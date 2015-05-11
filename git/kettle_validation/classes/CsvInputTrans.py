from KettleStep import KettleStep

__author__ = 'aoverton'


class CsvInput(KettleStep):
    """
    Models the CsvInput step. Relies heavily on members created in parent class

    """

    def __init__(self, data):
        """
        Call parent init and select relevant steps

        :param data: dict of step names and corresponding list of steps from trans/job
        :return: None
        """
        KettleStep.__init__(self)
        self.all_steps = data['steps']['CsvInput']

    def missing_encodings(self):
        """
        Missing encoding check

        :return: None
        """
        missing_encodings = filter(self.is_missing_encoding, self.all_steps)
        self.add_all_issues(missing_encodings, self.ERRORS, self.issue_messages.missing_encoding)

    def lazy_conversion(self):
        """
        Check if lazy conversions is used

        :return: None
        """
        field = "lazy_conversion"
        value = "y"
        lazy_steps = [step for step in self.all_steps if self.is_value(step, field, value)]
        self.add_all_issues(lazy_steps, self.WARNINGS, self.issue_messages.lazy_conversion)

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.missing_encodings()
        self.lazy_conversion()
        return self.issues
