import argparse
import sys
import logging
from collections import namedtuple
from classes import FtbImportV0Trans, FtbImportV1Trans
from classes import ShellJob
from parse_kettle_xml import ParseKettleXml
from classes.KettleStep import KettleStep as KS
from classes.IssueMessages import IssueMessages
from classes.PrettyColors import PrettyColors
from classes.get_files_from_path import get_files_from_path
from classes.custom_exceptions import FileNotFound, InvalidFileType

__author__ = 'aoverton'

PARSER_LOGGER = logging.getLogger(__name__)

class ImportMethodChecker():
    """
    Given a file or folder checks for the use datalogistics or PAPI imports

    """
    COLORIZER = PrettyColors()
    messages = IssueMessages()
    Endings = namedtuple("Endings", "trans job shell")
    endings = Endings(".ktr", ".kjb", ".sh")
    class_list_import = ['FtbImportV0Trans', 'FtbImportV1Trans']
    class_list_dl = ['ShellJob']

    def __init__(self):
        """
        Create an object that contains the appropriate member variables to store results

        :return: None
        """
        Endings = namedtuple("Endings", "trans job shell")
        self.Response = namedtuple("Response", "step issues")
        self.endings = Endings(".ktr", ".kjb", ".sh")
        self.ftb_import_vo_count = 0
        self.ftb_import_v1_count = 0
        self.data_logistics_count = 0

    def log_checks(self, results):
        """
        Print the results of the file checks using the logger

        :param results: A list of Response namedtuples
        :return: None
        """
        for result in results:
            notifications = result.issues[KS.NOTIFICATION]
            if len(notifications) > 0:
                for w in result.issues[KS.NOTIFICATION]:
                        PARSER_LOGGER.warning(self.COLORIZER.yellow("{}: {}".format(w.step_name, w.message)))

    def data_logistics_checks(self, data):
        """
        Run tests and collect results on use of data logistics

        :param data: dict where top level keys are categories of data parsed from transformation/job
        :return: None
        """
        results = []
        append = lambda x, y: results.append(self.Response(x, y))
        for test_class in self.class_list_dl:
            t = eval("{0}.{1}(data['steps'].get({0}.{1}.step_name, []))".format(test_class, test_class[:-3]))
            report = t.run_tests()
            append(test_class, report)
            for response in report[KS.NOTIFICATION]:
                if response.message == self.messages.data_logistics:
                    self.data_logistics_count += 1
        self.log_checks(results)

    def ftb_import_checks(self, data):
        """
        Run tests and collect results on use of PAPI imports

        :param data: dict where top level keys are categories of data parsed from transformation/job
        :return: None
        """
        results = []
        append = lambda x, y: results.append(self.Response(x, y))
        for test_class in self.class_list_import:
            t = eval("{0}.{1}(data['steps'].get({0}.{1}.step_name, []))".format(test_class, test_class[:-5]))
            report = t.run_tests()
            append(test_class, report)
            for response in report[KS.NOTIFICATION]:
                if response.message == self.messages.ftb_importv0:
                    self.ftb_import_vo_count += 1
                elif response.message == self.messages.ftb_importv1:
                    self.ftb_import_v1_count += 1
        self.log_checks(results)

    def shell_file_checks(self, file_path):
        """
        Run tests and collect results on use of datalogistcs in shell scripts

        :param file_path: file path to shell script to check
        :return: None
        """
        with open(file_path, "rU") as fp1:
            for line in fp1:
                if line.find("table_copy") != -1:
                    self.data_logistics_count += 1
                    PARSER_LOGGER.warning(self.COLORIZER.yellow("{}: {}".format(file_path,
                                                                                IssueMessages.data_logistics)))
                max_index = max(line.find("etl2prod"), line.find("prod2etl"))
                if max_index != -1:
                    self.data_logistics_count += 1
                    PARSER_LOGGER.warning(self.COLORIZER.yellow("{}: {}".format(file_path,
                                                                                IssueMessages.deprecated_dl)))

    def check_files(self, path):
        """
        Iterate through all files to be checked and pass them to the appropriate method to conduct checks

        :param path: path to file or folder to check
        :return: None
        """
        try:
            files = get_files_from_path(path, self.endings)
        except FileNotFound as e:
            PARSER_LOGGER.error(self.COLORIZER.red(e.message))
            sys.exit(1)
        except InvalidFileType as e:
            PARSER_LOGGER.error(self.COLORIZER.red(e.message))
            sys.exit(2)
        for file_path in files:
            if file_path.endswith(self.endings.trans):
                data = ParseKettleXml(file_path).parse_xml()
                self.ftb_import_checks(data)
            elif file_path.endswith(self.endings.job):
                data = ParseKettleXml(file_path).parse_xml()
                self.data_logistics_checks(data)
            elif file_path.endswith(self.endings.shell):
                self.shell_file_checks(file_path)

    def summary(self):
        """
        Create a summary of results from tests

        :return: dictionary of summarized results
        """
        dl_present = self.data_logistics_count > 0
        papi_import_present = self.ftb_import_vo_count > 0 or self.ftb_import_v1_count > 0
        return {'ftb_import_v0': self.ftb_import_vo_count,
                    'ftb_import_v1': self.ftb_import_v1_count,
                    'dl_count': self.data_logistics_count,
                    'dl_present': dl_present,
                    'papi_import_present': papi_import_present}


def main(path):
    """
    Runs import checks on provided path

    :param path: path to file or folder to check
    :return: dictionary of summarized results
    """
    checker = ImportMethodChecker()
    checker.check_files(path)
    return checker.summary()


def parse_args():
    """
    Parser for command line arguments

    :return: dictionary of command line arguments
    """
    parser = argparse.ArgumentParser(description='Check kettle files for use of datalogistis or PAPI imports')
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
