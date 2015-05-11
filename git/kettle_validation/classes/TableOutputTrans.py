from KettleStep import KettleStep

__author__ = 'aoverton'


class TableOutput(KettleStep):
    """
    Models the TableOutput step. Relies heavily on members created in parent class

    """

    def __init__(self, data):
        """
        Call parent init and select relevant steps

        :param data: dict of step names and corresponding list of steps from trans/job
        :return: None
        """
        KettleStep.__init__(self)
        self.all_steps = data['steps']['TableOutput']

    def ignore_errors(self):
        """
        Check if sql errors are ignored

        :return: None
        """
        field = "ignore_errors"
        value = "y"
        ignore_emptys = [step for step in self.all_steps if self.is_value(step, field, value)]
        self.add_all_issues(ignore_emptys, self.WARNINGS, self.issue_messages.ignore_insert_errors)

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.ignore_errors()
        return self.issues
