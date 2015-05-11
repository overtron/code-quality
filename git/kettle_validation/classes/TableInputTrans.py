from KettleStep import KettleStep

__author__ = 'aoverton'


class TableInput(KettleStep):
    """
    Models the TableInput step. Relies heavily on members created in parent class

    """
    def __init__(self, data):
        """
        Call parent init and select relevant steps

        :param data: dict of step names and corresponding list of steps from trans/job
        :return: None
        """
        KettleStep.__init__(self)
        self.all_steps = data['steps']['TableInput']

    def select_star(self):
        """
        Check if select * is used
        :return: None
        """
        field = "sql"
        value = "*"
        sql_steps = [step for step in self.all_steps if self.contains_value(step, field, value)]
        self.add_all_issues(sql_steps, self.WARNINGS, self.issue_messages.select_star)

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.limits_set()
        self.select_star()
        self.lazy_conversion("lazy_conversion_active")
        return self.issues
