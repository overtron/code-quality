'''
Created on Apr 6, 2015

@author: nnair

Python script to parse Kettle files and validate it against set standards
'''

import re
import sys
import logging
import argparse
import xml.etree.ElementTree as ET
from names_regex import DEFAULT_NAMES as DEFAULT_NAMES


# --------------------------------------------------------------------------------------------------


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

# --------------------------------------------------------------------------------------------------

PARSER_LOGGER = logging.getLogger(__name__)
logging.addLevelName(logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))

# --------------------------------------------------------------------------------------------------


def step_notes(root, type):
    """
    Find all notes in the root element of kettle file
    If there are no notes, fail
    :param root:
    """
    PARSER_LOGGER.info('Checking for notes')
    step_notes_passed = True
    notepads = root.findall('./notepads/notepad/note')
    if not notepads:
        step_notes_passed = False
    return step_notes_passed

# --------------------------------------------------------------------------------------------------


def evaluate_entries(entries):
    """
    If any name is the same as the default name return false
    :param entries:
    """
    step_names_passed = True
    evaluated = False
    for entryname in entries:
        PARSER_LOGGER.info('Checking entry {}'.format(entryname.text))
        for default_name in DEFAULT_NAMES:
            if re.findall(default_name, entryname.text):
                step_names_passed = False
                evaluated = True
                break
        if evaluated:
            break
    return step_names_passed

# --------------------------------------------------------------------------------------------------


def step_names(root, type):
    """
    Find all entries in root element
    check if they have non default names
    :param root:
    """
    PARSER_LOGGER.info('Checking Step Names')
    if type == "job":
        entries = root.findall('./entries/entry/name')
    elif type == "transformation":
        entries = root.findall('./step/name')

    PARSER_LOGGER.info('Found {} step(s) in the file'.format(len(entries)))

    step_names_passed = evaluate_entries(entries)

    return step_names_passed

# --------------------------------------------------------------------------------------------------


def evaluate_descriptions(entries):
    """
    If no description text fail check
    :param entries:
    """
    step_descriptions_passed = True
    for entrydesc in entries:
        if not entrydesc.text:
            step_descriptions_passed = False

    return step_descriptions_passed

# --------------------------------------------------------------------------------------------------


def step_descriptions(root, type):
    """
    Takes root element and finds descriptions
    If no descriptions exist for each entry - return False
    :param root:
    :returntype boolean:
    """
    PARSER_LOGGER.info('Checking descriptions')
    if type == "job":
        entries = root.findall('./entries/entry/description')
    else:
        entries = root.findall('./step/description')

    step_descriptions_passed = evaluate_descriptions(entries)
    return step_descriptions_passed

# --------------------------------------------------------------------------------------------------


def kettle_evaluate(root):
    evaluation_passed = True
    type = root.tag
    colorizer = PrettyColors()

    PARSER_LOGGER.info('Examining {}'.format(type))
    warning_count = 0
    # Examine if names are non-default
    if step_names(root, type):
        PARSER_LOGGER.info(colorizer.green('Step names check passed'))
    else:
        PARSER_LOGGER.error(colorizer.red('Step names checks failed'))

    # Examine if descriptions for all steps are filled
    if step_descriptions(root, type):
        PARSER_LOGGER.info(colorizer.green('Step descriptions check passed'))
    else:
        PARSER_LOGGER.warning(colorizer.yellow('Step descriptions check failed'))

    # Examine if there is a note
    if step_notes(root, type):
        PARSER_LOGGER.info(colorizer.green('Notes check passed'))
    else:
        PARSER_LOGGER.error(colorizer.red('Notes check failed'))
    return evaluation_passed

# --------------------------------------------------------------------------------------------------


def parse_command_line_args():
    parser = argparse.ArgumentParser(
        description='Parse the Kettle file evaluate against kettle standards')
    parser.add_argument('--filename', '-f', type=str, help='filename of the file to evaluate')

    return parser.parse_args()

# --------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    PARSER_LOGGER = logging.getLogger()
    PARSER_LOGGER.setLevel(logging.INFO)
    CONSOLE_HANDLER = logging.StreamHandler(sys.stdout)
    CONSOLE_HANDLER.setLevel(logging.INFO)
    CONSOLE_HANDLER.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    PARSER_LOGGER.addHandler(CONSOLE_HANDLER)

    CL_ARGS = parse_command_line_args()
    FILENAME = CL_ARGS.filename
    TREE = ET.parse(FILENAME)
    ROOT = TREE.getroot()
    kettle_evaluate(ROOT)
