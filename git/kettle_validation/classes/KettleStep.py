from collections import namedtuple

from custom_exceptions import InvalidIssueType
from IssueMessages import IssueMessages


__author__ = 'aoverton'


class KettleStep:
    """
    Parent class for all classes used to model checks for kettle tests

    """
    WARNINGS = "warnings"
    ERRORS = "errors"
    NOTIFICATION = "notifications"

    def __init__(self):
        """
        Initialize necessary structures

        :return: None
        """
        self.issues = {self.WARNINGS: [],
                       self.ERRORS: [],
                       self.NOTIFICATION: []}
        self.Issue = namedtuple('Issue', 'step_name message')
        self.issue_messages = IssueMessages()
        self.all_steps = []

    def add_issue(self, issue_type, kv_pair):
        """
        Add an issue to one of the defined categories in issues

        :param issue_type: level of issue to add. Type must already be defined in issues before using
        :param kv_pair: Issue namedtuple
        :return: None
        """
        if issue_type not in self.issues.keys():
            raise InvalidIssueType
        if isinstance(kv_pair, self.Issue):
            self.issues[issue_type].append(kv_pair)

    def add_all_issues(self, steps, issue_t, message):
        """
        Helper method to call add_issue for multiple issues

        :param steps: list of steps that have an issue
        :param issue_t: type of issue to add
        :param message: message to record with this issue
        :return: None
        """
        for step in steps:
            self.add_issue(issue_t, self.Issue(step.find("name").text, message))

    @staticmethod
    def is_missing_encoding(step):
        """
        Determines if a step has set an encoding.

        :param step: Step to check
        :return: true if encoding is missing, false otherwise
        """
        encoding = step.find("encoding").text
        if encoding is None or encoding == "":
            return True
        else:
            return False

    @staticmethod
    def is_limit_set(step):
        """
        Determines if a step has a limit set

        :param step: Step to check
        :return: true if limit set, false otherwise
        """
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
        """
        Determines if a step has files not set as required

        :param step: Step to check
        :return: true if a flag is found set to no, false otherwise
        """
        req_flags = step.find("file").findall("file_required")
        result = False
        for flag in req_flags:
            if flag.text.lower() == "n":
                result = True
        return result

    @staticmethod
    def is_value(step, field, value):
        """
        Determines if the given step's text value matches the given value in the given field. Not case-sensitive

        :param step: Step to check
        :param field: XML node to check
        :param value: Value to compare with text value of the field
        :return: true if text found, false otherwise
        """
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
        """
        Determines if the given step's text value contains the given value in the given field. Is case-sensitive

        :param step: Step to check
        :param field: XML node to check
        :param value: String or list of Strings with the value(s) to check
        :return: true if any value is found, false otherwise
        """
        if not isinstance(value, list):
            list_value = [value]
        else:
            list_value = value
        tag = step.find(field)
        result = False
        for val in list_value:
            if tag.text.find(val) != -1:
                result = True
        return result

    def text_files_not_required(self):
        """
        Check if text files are missing required flag

        :return: None
        """
        not_required = filter(self.is_file_missing_required_flag, self.all_steps)
        self.add_all_issues(not_required, self.WARNINGS, self.issue_messages.not_required)

    def limits_set(self):
        """
        Check if limit is used

        :return: None
        """
        set_limits = filter(self.is_limit_set, self.all_steps)
        self.add_all_issues(set_limits, self.ERRORS, self.issue_messages.limit_set)

    def missing_encodings(self):
        """
        Missing encoding check

        :return: None
        """
        missing_encodings = filter(self.is_missing_encoding, self.all_steps)
        self.add_all_issues(missing_encodings, self.ERRORS, self.issue_messages.missing_encoding)

    def existence(self, notification_level, message):
        """
        Check if the step exists

        :param notification_level: level of notification to add
        :param message: message to log with the issue
        :return: None
        """
        self.add_all_issues(self.all_steps, notification_level, message)

    def ignore_empty_file(self):
        """
        Check if step ignores empty files

        :return: None
        """
        field = "IsIgnoreEmptyFile"
        value = "y"
        ignore_emptys = [step for step in self.all_steps if self.is_value(step, field, value)]
        self.add_all_issues(ignore_emptys, self.WARNINGS, self.issue_messages.ignore_empty_file)

    def ignore_missing_file(self):
        """
        Check if step ignores missing files

        :return: None
        """
        field = "doNotFailIfNoFile"
        value = "y"
        ignore_emptys = [step for step in self.all_steps if self.is_value(step, field, value)]
        self.add_all_issues(ignore_emptys, self.WARNINGS, self.issue_messages.ignore_missing_file)

    def lazy_conversion(self, field):
        """
        Check if lazy conversions is used

        :param field: name of node to search for lazy conversion
        :return: None
        """
        value = "y"
        lazy_steps = [step for step in self.all_steps if self.is_value(step, field, value)]
        self.add_all_issues(lazy_steps, self.WARNINGS, self.issue_messages.lazy_conversion)