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

    def limits_set(self):
        """
        Check if limit is used

        :return: None
        """
        set_limits = filter(self.is_limit_set, self.all_steps)
        self.add_all_issues(set_limits, self.ERRORS, self.issue_messages.limit_set)

    def select_star(self):
        """
        Check if select * is used
        :return: None
        """
        field = "sql"
        value = "*"
        sql_steps = [step for step in self.all_steps if self.contains_value(step, field, value)]
        self.add_all_issues(sql_steps, self.WARNINGS, self.issue_messages.select_star)

    def lazy_conversion(self):
        """
        Check if lazy conversions is used

        :return: None
        """
        field = "lazy_conversion_active"
        value = "y"
        lazy_steps = [step for step in self.all_steps if self.is_value(step, field, value)]
        self.add_all_issues(lazy_steps, self.WARNINGS, self.issue_messages.lazy_conversion)

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.limits_set()
        self.select_star()
        self.lazy_conversion()
        return self.issues
