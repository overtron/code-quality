from KettleStep import KettleStep

__author__ = 'aoverton'


class JsonInput(KettleStep):
    """
    Models the JsonInput step. Relies heavily on members created in parent class

    """

    step_name = 'JsonInput'

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.limits_set()
        self.text_files_not_required()
        self.ignore_files("IsIgnoreEmptyFile", "y", self.WARNINGS, self.issue_messages.ignore_empty_file)
        self.ignore_files("doNotFailIfNoFile", "y", self.WARNINGS, self.issue_messages.ignore_missing_file)
        return self.issues