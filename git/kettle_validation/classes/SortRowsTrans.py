from KettleStep import KettleStep

__author__ = 'aoverton'


class SortRows(KettleStep):
    def __init__(self, data):
        KettleStep.__init__(self)
        self.all_steps = data['steps']['SortRows']
        if not isinstance(self.all_steps, list):
            self.all_steps = [self.all_steps]

    def unique_rows(self):
        field = "unique_rows"
        value = "y"
        unique_options = [step for step in self.all_steps if self.is_value(step, field, value)]
        self.add_all_issues(unique_options, self.WARNINGS, self.issue_messages.unique_rows)

    def run_tests(self):
        self.unique_rows()
        return self.issues
