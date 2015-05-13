from KettleStep import KettleStep

__author__ = 'aoverton'


class ExcelInput(KettleStep):
    """
    Models the ExcelInput step. Relies heavily on members created in parent class

    """

    step_name = 'ExcelInput'

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.missing_encodings()
        self.limits_set()
        self.text_files_not_required()
        return self.issues