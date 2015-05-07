from KettleStep import KettleStep

__author__ = 'aoverton'


class SelectValues(KettleStep):
    def __init__(self, data):
        KettleStep.__init__(self)
        self.all_steps = data['steps']['SelectValues']

    def is_multiple_tabs(self, step):
        paths = ['./fields/field/name', './fields/remove/name', './fields/meta/name']
        results = [step.find(path) for path in paths]
        counter = 0
        for result in results:
            if result is not None:
                counter += 1
        if counter > 1:
            return True
        else:
            return False

    def multiple_tabs(self):
        multi_tabs = [step for step in self.all_steps if self.is_multiple_tabs(step)]
        self.add_all_issues(multi_tabs, self.ERRORS, self.issue_messages.multi_tabs)

    def run_tests(self):
        self.multiple_tabs()
        return self.issues