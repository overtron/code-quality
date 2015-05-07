from KettleStep import KettleStep

__author__ = 'aoverton'


class TableOutput(KettleStep):
    def __init__(self, data):
        KettleStep.__init__(self)
        self.all_steps = data['steps']['TableOutput']

    def ignore_errors(self):
        field = "ignore_errors"
        value = "y"
        ignore_emptys = [step for step in self.all_steps if self.is_value(step, field, value)]
        self.add_all_issues(ignore_emptys, self.WARNINGS, self.issue_messages.ignore_insert_errors)

    def run_tests(self):
        self.ignore_errors()
        return self.issues
