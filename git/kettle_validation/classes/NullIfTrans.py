from KettleStep import KettleStep

__author__ = 'aoverton'


class NullIf(KettleStep):
    """
    Models the NullIf step. Relies heavily on members created in parent class

    """

    def __init__(self, data):
        """
        Call parent init and select relevant steps

        :param data: dict of step names and corresponding list of steps from trans/job
        :return: None
        """
        KettleStep.__init__(self)
        self.all_steps = data['steps']['NullIf']

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.existence(self.WARNINGS, self.issue_messages.null_steps)
        return self.issues
