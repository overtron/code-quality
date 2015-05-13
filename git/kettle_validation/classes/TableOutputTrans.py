from KettleStep import KettleStep

__author__ = 'aoverton'


class TableOutput(KettleStep):
    """
    Models the TableOutput step. Relies heavily on members created in parent class

    """

    step_name = 'TableOutput'

    def ignore_errors(self):
        """
        Check if sql errors are ignored

        :return: None
        """
        field = "ignore_errors"
        value = "y"
        ignore_emptys = [step for step in self.all_steps if self.is_value(step, field, value)]
        self.add_all_issues(ignore_emptys, self.WARNINGS, self.issue_messages.ignore_insert_errors)

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.ignore_errors()
        return self.issues
