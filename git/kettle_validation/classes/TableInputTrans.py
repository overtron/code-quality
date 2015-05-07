from KettleStep import KettleStep

__author__ = 'aoverton'


class TableInput(KettleStep):
    def __init__(self, data):
        KettleStep.__init__(self)
        self.all_steps = data['steps']['TableInput']

    def limits_set(self):
        set_limits = filter(self.is_limit_set, self.all_steps)
        self.add_all_issues(set_limits, self.ERRORS, self.issue_messages.limit_set)

    def select_star(self):
        field = "sql"
        value = "*"
        sql_steps = [step for step in self.all_steps if self.contains_value(step, field, value)]
        self.add_all_issues(sql_steps, self.WARNINGS, self.issue_messages.select_star)

    def lazy_conversion(self):
        field = "lazy_conversion_active"
        value = "y"
        lazy_steps = [step for step in self.all_steps if self.is_value(step, field, value)]
        self.add_all_issues(lazy_steps, self.WARNINGS, self.issue_messages.lazy_conversion)

    def run_tests(self):
        self.limits_set()
        self.select_star()
        self.lazy_conversion()
        return self.issues
