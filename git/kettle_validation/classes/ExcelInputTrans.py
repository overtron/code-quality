from KettleStep import KettleStep

__author__ = 'aoverton'


class ExcelInput(KettleStep):
    """
    Models the ExcelInput step. Relies heavily on members created in parent class

    """

    def __init__(self, data):
        """
        Call parent init and select relevant steps

        :param data: dict of step names and corresponding list of steps from trans/job
        :return: None
        """
        KettleStep.__init__(self)
        self.all_steps = data['steps']['ExcelInput']

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.missing_encodings()
        self.limits_set()
        self.text_files_not_required()
        return self.issues