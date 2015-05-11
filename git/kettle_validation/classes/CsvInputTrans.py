from KettleStep import KettleStep

__author__ = 'aoverton'


class CsvInput(KettleStep):
    """
    Models the CsvInput step. Relies heavily on members created in parent class

    """

    def __init__(self, data):
        """
        Call parent init and select relevant steps

        :param data: dict of step names and corresponding list of steps from trans/job
        :return: None
        """
        KettleStep.__init__(self)
        self.all_steps = data['steps']['CsvInput']

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.missing_encodings()
        self.lazy_conversion("lazy_conversion")
        return self.issues
