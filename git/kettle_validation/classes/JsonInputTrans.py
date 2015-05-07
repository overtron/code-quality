from KettleStep import KettleStep

__author__ = 'aoverton'


class JsonInput(KettleStep):
    def __init__(self, data):
        KettleStep.__init__(self)
        self.all_steps = data['steps']['JsonInput']

    def limits_set(self):
        set_limits = filter(self.is_limit_set, self.all_steps)
        self.add_all_issues(set_limits, self.ERRORS, self.issue_messages.limit_set)

    def text_files_not_required(self):
        not_required = filter(self.is_file_missing_required_flag, self.all_steps)
        self.add_all_issues(not_required, self.WARNINGS, self.issue_messages.not_required)

    def ignore_empty_file(self):
        field = "doNotFailIfNoFile"
        value = "y"
        ignore_emptys = [step for step in self.all_steps if self.is_value(step, field, value)]
        self.add_all_issues(ignore_emptys, self.WARNINGS, self.issue_messages.ignore_empty_file)

    def ignore_missing_file(self):
        field = "IsIgnoreEmptyFile"
        value = "y"
        ignore_emptys = [step for step in self.all_steps if self.is_value(step, field, value)]
        self.add_all_issues(ignore_emptys, self.WARNINGS, self.issue_messages.ignore_missing_file)

    def run_tests(self):
        self.limits_set()
        self.text_files_not_required()
        self.ignore_empty_file()
        self.ignore_missing_file()
        return self.issues