from KettleStep import KettleStep

__author__ = 'aoverton'


class MysqlBulkLoader(KettleStep):
    def __init__(self, data):
        KettleStep.__init__(self)
        self.all_steps = data['steps']['MySQLBulkLoader']

    def select_star(self):
        field = "fifo_file_name"
        value = "/tmp/fifo"
        bulk_steps = [step for step in self.all_steps if self.contains_value(step, field, value)]
        self.add_all_issues(bulk_steps, self.ERRORS, self.issue_messages.default_fifo)

    def existence(self):
        self.add_all_issues(self.all_steps, self.WARNINGS, self.issue_messages.bulk_loader)

    def run_tests(self):
        self.select_star()
        self.existence()
        return self.issues
