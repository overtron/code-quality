from KettleStep import KettleStep

__author__ = 'aoverton'


class Shell(KettleStep):
    def __init__(self, data):
        KettleStep.__init__(self)
        self.all_steps = data['steps']['SHELL']

    def using_data_logistics(self):
        using_dl = []
        external_script = []
        field = "insertScript"
        value = "y"
        search_field = "script"
        search_value_1 = "table_copy"
        search_value_2 = "etl2prod"
        search_value_3 = "prod2etl"
        for step in self.all_steps:
            if self.is_value(step, field, value):
                if self.contains_value(step, search_field, search_value_1) \
                        or self.contains_value(step, search_field, search_value_2) \
                        or self.contains_value(step, search_field, search_value_3):
                    using_dl.append(step)
            else:
                external_script.append(step)
        self.add_all_issues(using_dl, self.NOTIFICATION, self.issue_messages.data_logistics)
        self.add_all_issues(external_script, self.NOTIFICATION, self.issue_messages.external_script)

    def run_tests(self):
        self.using_data_logistics()
        return self.issues
