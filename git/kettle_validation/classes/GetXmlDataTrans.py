from KettleStep import KettleStep

__author__ = 'aoverton'


class GetXmlData(KettleStep):
    """
    Models the getXMLData step. Relies heavily on members created in parent class

    """

    def __init__(self, data):
        """
        Call parent init and select relevant steps

        :param data: dict of step names and corresponding list of steps from trans/job
        :return: None
        """
        KettleStep.__init__(self)
        self.all_steps = data['steps']['getXMLData']

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.limits_set()
        self.text_files_not_required()
        self.ignore_empty_file()
        self.ignore_missing_file()
        return self.issues