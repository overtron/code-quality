from KettleStep import KettleStep

__author__ = 'aoverton'


class GetXmlData(KettleStep):
    """
    Models the getXMLData step. Relies heavily on members created in parent class

    """

    def __init__(self, data):
        """
        Call parent init and select relevant steps

        :param data: dict of step names and corresponding list of steps from trans/job
        :return: None
        """
        KettleStep.__init__(self)
        self.all_steps = data['steps']['getXMLData']

    def limits_set(self):
        """
        Check if limit is used

        :return: None
        """
        set_limits = filter(self.is_limit_set, self.all_steps)
        self.add_all_issues(set_limits, self.ERRORS, self.issue_messages.limit_set)

    def text_files_not_required(self):
        """
        Check if text files are missing required flag

        :return: None
        """
        not_required = filter(self.is_file_missing_required_flag, self.all_steps)
        self.add_all_issues(not_required, self.WARNINGS, self.issue_messages.not_required)

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

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.limits_set()
        self.text_files_not_required()
        self.ignore_empty_file()
        self.ignore_missing_file()
        return self.issues