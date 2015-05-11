from KettleStep import KettleStep

__author__ = 'aoverton'


class TextFileOutput(KettleStep):
    """
    Models the TextFileOutput step. Relies heavily on members created in parent class

    """

    def __init__(self, data):
        """
        Call parent init and select relevant steps

        :param data: dict of step names and corresponding list of steps from trans/job
        :return: None
        """
        KettleStep.__init__(self)
        self.all_steps = data['steps']['TextFileOutput']

    def incorrect_encoding(self):
        """
        Check for non UTF-8 encodings

        :return:
        """
        field = "encoding"
        value = "UTF-8"
        # is_value is negated below to function as is_not_value
        incorrect_encodings = [step for step in self.all_steps if not self.is_value(step, field, value)]
        self.add_all_issues(incorrect_encodings, self.ERRORS, self.issue_messages.missing_utf_8)

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.incorrect_encoding()
        return self.issues
