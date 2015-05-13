from KettleStep import KettleStep

__author__ = 'aoverton'


class CsvInput(KettleStep):
    """
    Models the CsvInput step. Relies heavily on members created in parent class

    """

    step_name = 'CsvInput'

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.missing_encodings()
        self.lazy_conversion("lazy_conversion")
        return self.issues
