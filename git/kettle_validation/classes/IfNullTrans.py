from KettleStep import KettleStep

__author__ = 'aoverton'


class IfNull(KettleStep):
    """
    Models the IfNull step. Relies heavily on members created in parent class

    """

    step_name = 'IfNull'

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.existence(self.WARNINGS, self.issue_messages.null_steps)
        return self.issues
