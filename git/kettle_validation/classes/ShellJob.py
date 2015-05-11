from KettleStep import KettleStep

__author__ = 'aoverton'


class Shell(KettleStep):
    """
    Models the SHELL step. Relies heavily on members created in parent class

    """

    def __init__(self, data):
        """
        Call parent init and select relevant steps

        :param data: dict of step names and corresponding list of steps from trans/job
        :return: None
        """
        KettleStep.__init__(self)
        self.all_steps = data['steps']['SHELL']

    def using_data_logistics(self):
        """
        Check if datalogistics is being used with a distinction between current and deprecated versions

        :return: None
        """
        using_table_copy = []
        using_old_dl = []
        external_script = []
        field = "insertScript"
        value = "y"
        for step in self.all_steps:
            if self.is_value(step, field, value):
                search_field = "script"
                search_value_table_copy = "table_copy"
                search_value_old_dl = ["etl2prod", "prod2etl"]
                if self.contains_value(step, search_field, search_value_table_copy):
                    using_table_copy.append(step)
                if self.contains_value(step, search_field, search_value_old_dl):
                    using_old_dl.append(step)
            else:
                external_script.append(step)
        self.add_all_issues(using_table_copy, self.NOTIFICATION, self.issue_messages.data_logistics)
        self.add_all_issues(using_old_dl, self.NOTIFICATION, self.issue_messages.deprecated_dl)
        self.add_all_issues(external_script, self.NOTIFICATION, self.issue_messages.external_script)

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.using_data_logistics()
        return self.issues
