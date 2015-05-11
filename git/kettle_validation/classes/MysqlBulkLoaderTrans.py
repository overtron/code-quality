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

    def default_pipe(self):
        """
        Checks for use of default pipe

        :return: None
        """
        field = "fifo_file_name"
        value = "/tmp/fifo"
        bulk_steps = [step for step in self.all_steps if self.contains_value(step, field, value)]
        self.add_all_issues(bulk_steps, self.ERRORS, self.issue_messages.default_fifo)

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.default_pipe()
        self.existence(self.WARNINGS, self.issue_messages.bulk_loader)
        return self.issues
