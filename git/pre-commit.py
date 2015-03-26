#!/usr/bin/env python
from __future__ import with_statement
import os
import re
import shutil
import subprocess
import sys
import tempfile
import linecache

_PEP_WARN = re.compile(r"\bW\d+\b")
_PEP_ERROR = re.compile(r"\bE\d+\b")
_PEP_LOCATION = re.compile(r"py:(\d+):(\d+): ")

_PYLINT_WARN = re.compile(r"^W:")
_PYLINT_ERROR = re.compile(r"^(E|F):")
_PYLINT_CONVENTION = re.compile(r"^(C|R):")
_PYLINT_LOCATION = re.compile(r"(C|R|W|E|F):\s*(\d+),\s*(\d+): ")
_PYLINT_LENGTH = re.compile(r"\(line-too-long\)$")
_PYLINT_SCORE = re.compile(r"Your code has been rated at ([\d\.]+)/10")

GIT_DIFF_REGEXES = [
    re.compile(r"@ -(\d+) \+(\d+) @"),  # matches @@ -# +# @@ style
    re.compile(r"@ -(\d+\,\d+) \+(\d+) @"),  # matches @@ -#,# +# @@ style
    re.compile(r"@ -(\d+) \+(\d+\,\d+) @"),  # matches @@ -# +#,# @@ style
    re.compile(r"@ -(\d+\,\d+) \+(\d+,\d+) @")  # matches @@ -#,# +#,# @@ style
]

WARNING = 'warning'
ERROR = 'error'
CONVENTION = 'convention'


class PrettyColors(object):
    colors = {
        'red': '\033[1;31m',
        'green': '\033[1;32m',
        'yellow': '\033[1;33m',
        'cyan': '\033[0;36m',
        'off': '\033[0m'
    }

    def colorize(self, text, color):
        return self.colors[color] + text + self.colors['off']

    def red(self, text):
        return self.colorize(text, 'red')

    def cyan(self, text):
        return self.colorize(text, 'cyan')

    def green(self, text):
        return self.colorize(text, 'green')

    def yellow(self, text):
        return self.colorize(text, 'yellow')

    def format(self, text, issue_type):
        """
        :param text: the text you want to print
        :param issue_type: the type of issue (warning, error, convention)
        :return: the colored text
        """
        if issue_type == WARNING:
            return self.yellow(text)
        elif issue_type == ERROR:
            return self.red(text)
        elif issue_type == CONVENTION:
            return self.cyan(text)
        else:
            return text


def parse_range(range_item):
    try:  # format is either #,# or #
        begin, length = range_item.split(',')
    except Exception:
        begin = range_item
        length = 1
    return range(int(begin), int(begin) + int(length))


def parse_ranges(ranges):
    return [parse_range(range_item[1]) for range_item in ranges]


def check_bad_characters(diff_lines, full_path):
    diff_output = None
    try:
        diff_output = diff_lines.decode('utf8')
    except UnicodeDecodeError:
        # this fails on macs because -P was removed because steve jobs is pure evil
        grep_cmd = "perl --color='auto' -P -n \"" + r"[\x80-\xFF]" + "\" " + full_path
        # SO WE'RE USING PERL INSTEAD LOL
        perl_cmd = "perl -ane '{ if(m/[[:^ascii:]]/) { print  } }' " + full_path
        perl = subprocess.Popen(perl_cmd, stdout=subprocess.PIPE, shell=True)
        output = perl.stdout.readlines()
        perl_result = '\n'.join([x.decode('utf8') for x in output])

        print ' '.join(['There is a bad character in %s.' % full_path,
                        'Please remove the character and commit again.',
                        'Your character is probably somewhere in these lines\n %s' % perl_result])
        print ' '.join(['Try executing {} (ubuntu)'.format(grep_cmd),
                        'or {} (mac, ubuntu) to find the characters'.format(perl_cmd)])
        print ' '.join(['If you absolutely require the character,',
                        'fix all other changes and use the',
                        '--no-verify flag in your commit command.'])
    return diff_output


def get_changed_lines(path):
    full_path = os.path.join(os.getcwd(), path.strip())
    # git diff --no-ext-diff --cached -U0 <filename>
    diff = subprocess.Popen(['git', 'diff', '--no-ext-diff', '--cached', '-U0', full_path],
                            stdout=subprocess.PIPE)
    (result, _) = diff.communicate()

    diff_output = check_bad_characters(result, full_path)
    if diff_output is None:
        sys.exit(1)

    lines = []
    for diff_regex in GIT_DIFF_REGEXES:
        diff_matches = diff_regex.findall(diff_output)
        ranges = parse_ranges(diff_matches)
        for rng in ranges:
            for line in rng:
                lines.append(int(line))

    return lines


def check_for_git_difftext(filepath):
    colorizer = PrettyColors()
    bad_lines = []
    changed_lines = get_changed_lines(filepath)

    for line in changed_lines:
        line_text = linecache.getline(filepath, line)
        if '<<<<<' in line_text or '>>>>>' in line_text or '=======' in line_text:
            bad_lines.append('(%s) Line %d: %s' % (filepath, line, line_text))

    # Verify that markup wasn't left after a merge
    if len(bad_lines) > 0:
        print colorizer.red(' '.join(['You appear to have left git merge markup,',
                                      '<<<<< like this >>>>>.',
                                      'Please complete the merge or ask for help.']))
        for line in bad_lines:
            print colorizer.red(line.replace('\n', ''))
        sys.exit(1)


def system(*args, **kwargs):
    kwargs.setdefault('stdout', subprocess.PIPE)
    proc = subprocess.Popen(args, **kwargs)
    out, err = proc.communicate()
    return out


def get_location(line, is_pep=True):
    if is_pep:
        loc_matches = _PEP_LOCATION.search(line)
        cleaned_line = _PEP_LOCATION.sub('', line)
    else:
        loc_matches = _PYLINT_LOCATION.search(line)
        cleaned_line = _PYLINT_LOCATION.sub('', line)

    line_num = None
    col_offset = None
    if loc_matches:
        num_matches = len(loc_matches.groups())
        if num_matches >= 2:
            try:
                line_num = int(loc_matches.group(num_matches - 1))
                col_offset = int(loc_matches.group(num_matches))
            except Exception:
                pass

    return line_num, col_offset, cleaned_line


def clean_line(line, is_pep=True):
    line_num, col_offset, cleaned_line = get_location(line, is_pep)

    if line_num and col_offset is not None:
        line = 'Line:%4d, Column:%3d:  %s' % (line_num, col_offset, cleaned_line)
    else:
        return None

    return line


def get_pylint_type(line):
    if _PYLINT_WARN.search(line):
        return WARNING
    elif _PYLINT_ERROR.search(line):
        return ERROR
    elif _PYLINT_LENGTH.search(line):
        return ERROR
    if _PYLINT_CONVENTION.search(line):
        return CONVENTION
    else:
        return ''


def get_pep_type(line):
    if _PEP_WARN.search(line):
        return WARNING
    elif _PEP_ERROR.search(line):
        return ERROR
    else:
        return ''


def print_summary(colorizer, issue_counts):
    print colorizer.green('\n=== SUMMARY ===')
    for issue_type, issue_cnt in issue_counts.iteritems():
        if issue_type:
            print colorizer.format("%10s: %3d" % (issue_type, issue_cnt), issue_type)
    print '\n'


def show_pep_output(output):
    colorizer = PrettyColors()

    issue_counts = {
        WARNING: 0,
        ERROR: 0,
        '': 0
    }

    print colorizer.green('\n\nPEP8:')
    for line in output:
        line = clean_line(line, True)

        if line:
            out_type = get_pep_type(line)
            issue_counts[out_type] += 1
            print colorizer.format(line, out_type)

    print_summary(colorizer, issue_counts)
    return issue_counts[ERROR]


def print_code_score(colorizer, code_score):
    if code_score:
        score_txt = '\n\tGlobal code score: {} / 10.0'.format(code_score)
        if code_score < 2.5:
            colorized_txt = colorizer.red(score_txt)
        elif code_score < 5.0:
            colorized_txt = colorizer.yellow(score_txt)
        else:
            colorized_txt = colorizer.green(score_txt)

        print colorized_txt


def show_pylint_output(output, file_path, code_score=None):
    colorizer = PrettyColors()

    issue_counts = {
        WARNING: 0,
        ERROR: 0,
        CONVENTION: 0,
        '': 0
    }

    print colorizer.green('\n\nPylint: {}'.format(file_path))
    for line in output:
        out_type = get_pylint_type(line)
        line = clean_line(line, False)

        if line:
            issue_counts[out_type] += 1
            print colorizer.format(line, out_type)

    print_code_score(colorizer, code_score)
    print_summary(colorizer, issue_counts)
    return issue_counts[ERROR]


def get_pylint_report(pylint_out):

    code_score = None
    is_report = False
    report = []
    for line in pylint_out:
        if 'report' in line.lower():
            is_report = True

        if is_report:
            report.append(line)
            code_score_match = _PYLINT_SCORE.search(line)
            if code_score_match:
                try:
                    code_score = float(code_score_match.group(1))
                except Exception:
                    pass

    return '\n'.join(report), code_score


def run_pylint(git_root, file_path):
    report = None

    try:
        full_path = os.path.dirname(os.path.realpath(__file__))
        pylint_out = system('pylint', '--rcfile=%s' % os.path.join(full_path, 'pylintrc'), file_path)
        pylint_out = pylint_out.split('\n')

        report, code_score = get_pylint_report(pylint_out)
        error_count = show_pylint_output(pylint_out, file_path, code_score)
    except OSError:
        # pylint is not installed
        error_count = 0
        print 'pylint is not installed!'
        print '\thttp://www.pylint.org/#install'

    return error_count, report


def get_git_root_dir():
    git_root = system('git', 'rev-parse', '--show-toplevel')
    return git_root.strip()


def get_python_files(git_root, files):
    re_py = re.compile('^#!.*python$')

    py_files = []
    for file_name in files:
        base_file, file_ext = os.path.splitext(file_name)
        if file_ext.lower() == '.py':
            py_files.append(file_name)
        else:
            first_row = system('head', '-1', os.path.join(git_root, file_name))
            if re_py.search(first_row):
                py_files.append(file_name)

    return py_files


def main():
    git_root = get_git_root_dir()
    # modified = re.compile(r'^[AM]+\s+(?P<name>.*\.py)', re.MULTILINE)
    modified = re.compile(r'^[AM]+\s+(?P<name>.*)', re.MULTILINE)

    files = system('git', 'status', '--porcelain')
    files = modified.findall(files)
    files = get_python_files(git_root, files)

    tempdir = tempfile.mkdtemp()
    pylint_errors = 0
    for name in files:
        filename = os.path.join(tempdir, name)
        file_path = os.path.dirname(filename)
        actual_file = os.path.join(git_root, name)

        check_for_git_difftext(actual_file)
        pylint_error, pylint_report = run_pylint(git_root, actual_file)
        pylint_errors += pylint_error

        if not os.path.exists(file_path):
            os.makedirs(file_path)

        with file(filename, 'w') as fout:
            system('git', 'show', ':' + name, stdout=fout)

    # output = system('pep8', '.', cwd=tempdir)
    shutil.rmtree(tempdir)

    if pylint_errors > 0:
        print ' '.join(['\nYour commit did not go through,',
                       'please fix these errors and then recommit'])
        sys.exit(1)


if __name__ == '__main__':
    main()
