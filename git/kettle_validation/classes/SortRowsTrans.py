from KettleStep import KettleStep

__author__ = 'aoverton'


class SortRows(KettleStep):
    """
    Models the SortRows step. Relies heavily on members created in parent class

    """

    step_name = 'SortRows'

    def unique_rows(self):
        """
        Check if unique rows option is used

        :return: None
        """
        field = "unique_rows"
        value = "y"
        unique_options = [step for step in self.all_steps if self.is_value(step, field, value)]
        self.add_all_issues(unique_options, self.WARNINGS, self.issue_messages.unique_rows)

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.unique_rows()
        return self.issues
