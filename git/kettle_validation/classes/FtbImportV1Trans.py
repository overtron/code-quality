from KettleStep import KettleStep

__author__ = 'aoverton'


class FtbImportV1(KettleStep):
    """
    Modesl the FTBImportPluginV1 step. Relies heavily on members created in parent class
    """

    def __init__(self, data):
        """
        Call parent init and select relevant steps

        :param data: dict of step names and corresponding list of steps from trans/job
        :return: None
        """
        KettleStep.__init__(self)
        self.all_steps = data['steps']['FTBImportPluginV1']

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.existence(self.NOTIFICATION, self.issue_messages.ftb_importv1)
        return self.issues
