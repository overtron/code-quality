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


__author__ = 'aoverton'

PARSER_LOGGER = logging.getLogger(__name__)

class ImportMethodChecker():
    COLORIZER = PrettyColors()
    messages = IssueMessages()
    Endings = namedtuple("Endings", "trans job shell")
    endings = Endings(".ktr", ".kjb", ".sh")
    class_list_import = ['FtbImportV0Trans', 'FtbImportV1Trans']
    class_list_dl = ['ShellJob']

    def __init__(self):
        Endings = namedtuple("Endings", "trans job shell")
        self.Response = namedtuple("Response", "step issues")
        self.endings = Endings(".ktr", ".kjb", ".sh")
        self.ftb_import_vo_count = 0
        self.ftb_import_v1_count = 0
        self.data_logistics_count = 0

    def log_checks(self, results):
        for result in results:
            notifications = result.issues[KS.NOTIFICATION]
            if len(notifications) > 0:
                for w in result.issues[KS.NOTIFICATION]:
                        PARSER_LOGGER.warning(self.COLORIZER.yellow("{}: {}".format(w.step_name, w.message)))

    def data_logistics_checks(self, data):
        results = []
        append = lambda x, y: results.append(self.Response(x, y))
        for test_class in self.class_list_dl:
            t = eval("{}.{}(data)".format(test_class, test_class[:-3]))
            report = t.run_tests()
            append(test_class, report)
            for response in report[KS.NOTIFICATION]:
                if response.message == self.messages.data_logistics:
                    self.data_logistics_count += 1
        self.log_checks(results)

    def ftb_import_checks(self, data):
        results = []
        append = lambda x, y: results.append(self.Response(x, y))
        for test_class in self.class_list_import:
            t = eval("{}.{}(data)".format(test_class, test_class[:-5]))
            report = t.run_tests()
            append(test_class, report)
            for response in report[KS.NOTIFICATION]:
                if response.message == self.messages.ftb_importv0:
                    self.ftb_import_vo_count += 1
                elif response.message == self.messages.ftb_importv1:
                    self.ftb_import_v1_count += 1
        self.log_checks(results)

    def shell_file_checks(self, file_path):
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
        files = get_files_from_path(path, self.endings)
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
        dl_present = self.data_logistics_count > 0
        papi_import_present = self.ftb_import_vo_count > 0 or self.ftb_import_v1_count > 0
        return {'ftb_import_v0': self.ftb_import_vo_count,
                    'ftb_import_v1': self.ftb_import_v1_count,
                    'dl_count': self.data_logistics_count,
                    'dl_present': dl_present,
                    'papi_import_present': papi_import_present}


def main(path):
    checker = ImportMethodChecker()
    checker.check_files(path)
    return checker.summary()


def parse_args():
    parser = argparse.ArgumentParser(description='Get parsing parameters for kettle checker')
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
