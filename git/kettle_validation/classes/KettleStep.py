from collections import namedtuple

from custom_exceptions import InvalidIssueType
from IssueMessages import IssueMessages


__author__ = 'aoverton'


class KettleStep:
    WARNINGS = "warnings"
    ERRORS = "errors"
    NOTIFICATION = "notifications"

    def __init__(self):
        self.issues = {self.WARNINGS: [],
                       self.ERRORS: [],
                       self.NOTIFICATION: []}
        self.Issue = namedtuple('Issue', 'step_name message')
        self.issue_messages = IssueMessages()
        self.all_steps = []

    def add_issue(self, issue_type, kv_pair):
        if issue_type not in self.issues.keys():
            raise InvalidIssueType
        if isinstance(kv_pair, self.Issue):
            self.issues[issue_type].append(kv_pair)

    def add_all_issues(self, steps, issue_t, message):
        for step in steps:
            self.add_issue(issue_t, self.Issue(step.find("name").text, message))

    @staticmethod
    def is_missing_encoding(step):
        encoding = step.find("encoding").text
        if encoding is None or encoding == "":
            return True
        else:
            return False

    @staticmethod
    def is_limit_set(step):
        try:
            limit = int(step.find("limit").text)
        except TypeError:
            return False
        if limit > 0:
            return True
        else:
            return False

    @staticmethod
    def is_file_missing_required_flag(step):
        req_flags = step.find("file").findall("file_required")
        result = False
        for flag in req_flags:
            if flag.text.lower() == "n":
                result = True
        return result

    @staticmethod
    def is_value(step, field, value):
        tag = step.find(field)
        try:
            if tag.text.lower() == value.lower():
                return True
            else:
                return False
        except AttributeError:
            return False

    @staticmethod
    def contains_value(step, field, value):
        tag = step.find(field)
        if tag.text.find(value) == -1:
            return False
        else:
            return True