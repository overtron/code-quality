import argparse
import sys
import logging
from collections import namedtuple
# import * is used below to avoid maintaining a list of tests. See classes/__init__.py for imported classes
from classes import *
from classes.PrettyColors import PrettyColors
from classes.KettleStep import KettleStep as KS
from parse_kettle_xml import ParseKettleXml
from classes.get_files_from_path import get_files_from_path
from classes import class_list_trans


__author__ = 'aoverton'

PARSER_LOGGER = logging.getLogger(__name__)

class KettleChecker():
    """
    Given a file or folder runs a set of code quality checks on all .ktr and .kjb files found

    """
    COLORIZER = PrettyColors()

    def __init__(self, path):
        """
        Create an object that contains a list of valid files to check and member variables to store results

        :param path: path to file or folder to check
        :return None
        """
        Endings = namedtuple("Endings", "trans job")
        self.Response = namedtuple("Response", "step issues")
        self.endings = Endings(".ktr", ".kjb")
        self.errors_present = 0
        self.warnings_present = 0
        self.files = get_files_from_path(path, self.endings)

    def log_checks(self, results):
        """
        Print the results of the file checks using the logger

        :param results: A list of Response namedtuples
        :return None
        """
        for result in results:
            errors = len(result.issues[KS.ERRORS])
            warnings = len(result.issues[KS.WARNINGS])
            if errors > 0 or warnings > 0:
                PARSER_LOGGER.info(self.COLORIZER.green("Report for: {} Checks".format(result.step)))
                if errors > 0:
                    for w in result.issues[KS.ERRORS]:
                        PARSER_LOGGER.error(self.COLORIZER.red("{}: {}".format(w.step_name, w.message)))
                if warnings > 0:
                    for w in result.issues[KS.WARNINGS]:
                        PARSER_LOGGER.warning(self.COLORIZER.yellow("{}: {}".format(w.step_name, w.message)))

    def summarize(self):
        """
        Print a summary of all warnings and errors for a file or folder using the logger

        :return None
        """
        print "\n\n"
        PARSER_LOGGER.info("============= SUMMARY ===============")
        if self.errors_present > 0:
            if self.errors_present == 1:
                word_choice = "error"
            else:
                word_choice = "errors"
            PARSER_LOGGER.error(self.COLORIZER.red('Found {} validation {}'.format(self.errors_present, word_choice)))
        else:
            PARSER_LOGGER.info(self.COLORIZER.green("No validation errors found"))

        if self.warnings_present > 0:
            if self.warnings_present == 1:
                word_choice = "warning"
            else:
                word_choice = "warnings"
            PARSER_LOGGER.warning(self.COLORIZER.yellow('Found {} validation {}'
                                                        .format(self.warnings_present, word_choice)))
        else:
            PARSER_LOGGER.info(self.COLORIZER.green("No validation warnings found"))

    def transformation_checks(self, data):
        """
        Iterate through all of the transformation tests

        :param data: dictionary where keys are step types and values are a list of those step types from the
        transformation
        :return: None
        """
        results = []
        append = lambda x, y: results.append(self.Response(x, y))
        for test_class in class_list_trans:
            t = eval("{}.{}(data)".format(test_class, test_class[:-5]))
            report = t.run_tests()
            self.errors_present += len(report[KS.ERRORS])
            self.warnings_present += len(report[KS.WARNINGS])
            append(test_class, report)
        self.log_checks(results)

    def job_checks(self, root):
        pass

    def check_files(self):
        """
        Iterate through all files to be checked and pass them to the appropriate method to conduct checks

        :return: None
        """
        for file_path in self.files:
            print "\n\n"
            PARSER_LOGGER.info("KETTLE VALIDATOR: {}".format(file_path))
            data = ParseKettleXml(file_path).parse_xml()
            if file_path.endswith(self.endings.trans):
                self.transformation_checks(data)
            elif file_path.endswith(self.endings.job):
                self.job_checks(data)
        self.summarize()
        print self.COLORIZER.green("kettle_validator checks complete")


def main(path):
    """
    Runs all kettle checks on provided path

    :param path: path to file or folder to check
    :return: integer that is count of total number of errors found
    """
    checker = KettleChecker(path)
    checker.check_files()
    return checker.errors_present


def parse_args():
    """
    Parser for command line arguments

    :return: dictionary of command line arguments
    """
    parser = argparse.ArgumentParser(description='Check kettle files for common errors and design flaws')
    parser.add_argument('path', help='Path to folder or file to run the checker on')
    return vars(parser.parse_args())

if __name__ == "__main__":
    PARSER_LOGGER = logging.getLogger()
    PARSER_LOGGER.setLevel(logging.INFO)
    CONSOLE_HANDLER = logging.StreamHandler(sys.stdout)
    CONSOLE_HANDLER.setLevel(logging.INFO)
    CONSOLE_HANDLER.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    PARSER_LOGGER.addHandler(CONSOLE_HANDLER)
    logging.addLevelName(logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))
    args = parse_args()
    main(args['path'])
