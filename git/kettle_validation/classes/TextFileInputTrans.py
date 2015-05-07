from KettleStep import KettleStep

__author__ = 'aoverton'


class TextFileInput(KettleStep):
    def __init__(self, data):
        KettleStep.__init__(self)
        self.all_steps = data['steps']['TextFileInput']

    def missing_encodings(self):
        missing_encodings = filter(self.is_missing_encoding, self.all_steps)
        self.add_all_issues(missing_encodings, self.ERRORS, self.issue_messages.missing_encoding)

    def limits_set(self):
        set_limits = filter(self.is_limit_set, self.all_steps)
        self.add_all_issues(set_limits, self.ERRORS, self.issue_messages.limit_set)

    def text_files_not_required(self):
        not_required = filter(self.is_file_missing_required_flag, self.all_steps)
        self.add_all_issues(not_required, self.WARNINGS, self.issue_messages.not_required)

    def run_tests(self):
        self.missing_encodings()
        self.limits_set()
        self.text_files_not_required()
        return self.issues
