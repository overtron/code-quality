from KettleStep import KettleStep

__author__ = 'aoverton'


class SelectValues(KettleStep):
    """
    Models the SelectValues step. Relies heavily on members created in parent class

    """

    def __init__(self, data):
        """
        Call parent init and select relevant steps

        :param data: dict of step names and corresponding list of steps from trans/job
        :return: None
        """
        KettleStep.__init__(self)
        self.all_steps = data['steps']['SelectValues']

    def is_multiple_tabs(self, step):
        """
        Determine if multiple tabs are used

        :param step: Step to check
        :return: true if multiple tabs used, false otherwise
        """
        paths = ['./fields/field/name', './fields/remove/name', './fields/meta/name']
        results = [step.find(path) for path in paths]
        counter = 0
        for result in results:
            if result is not None:
                counter += 1
        if counter > 1:
            return True
        else:
            return False

    def multiple_tabs(self):
        """
        Checks if multiple tabs are used

        :return: None
        """
        multi_tabs = [step for step in self.all_steps if self.is_multiple_tabs(step)]
        self.add_all_issues(multi_tabs, self.ERRORS, self.issue_messages.multi_tabs)

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.multiple_tabs()
        return self.issues