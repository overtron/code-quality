from KettleStep import KettleStep

__author__ = 'aoverton'


class NullIf(KettleStep):
    """
    Models the NullIf step. Relies heavily on members created in parent class

    """

    step_name = 'NullIf'

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.existence(self.WARNINGS, self.issue_messages.null_steps)
        return self.issues
