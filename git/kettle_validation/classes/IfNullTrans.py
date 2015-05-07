from KettleStep import KettleStep

__author__ = 'aoverton'


class IfNull(KettleStep):
    def __init__(self, data):
        KettleStep.__init__(self)
        self.all_steps = data['steps']['IfNull']

    def existence(self):
        self.add_all_issues(self.all_steps, self.WARNINGS, self.issue_messages.null_steps)

    def run_tests(self):
        self.existence()
        return self.issues
