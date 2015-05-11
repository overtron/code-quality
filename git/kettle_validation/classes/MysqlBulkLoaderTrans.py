from KettleStep import KettleStep

__author__ = 'aoverton'


class MysqlBulkLoader(KettleStep):
    """
    Models the MySQLBulkLoader step. Relies heavily on members created in parent class

    """

    def __init__(self, data):
        """
        Call parent init and select relevant steps

        :param data: dict of step names and corresponding list of steps from trans/job
        :return: None
        """
        KettleStep.__init__(self)
        self.all_steps = data['steps']['MySQLBulkLoader']

    def select_star(self):
        """
        Checks for uses of select *

        :return: None
        """
        field = "fifo_file_name"
        value = "/tmp/fifo"
        bulk_steps = [step for step in self.all_steps if self.contains_value(step, field, value)]
        self.add_all_issues(bulk_steps, self.ERRORS, self.issue_messages.default_fifo)

    def existence(self):
        """
        Check if the step exists

        :return: None
        """
        self.add_all_issues(self.all_steps, self.WARNINGS, self.issue_messages.bulk_loader)

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.select_star()
        self.existence()
        return self.issues
