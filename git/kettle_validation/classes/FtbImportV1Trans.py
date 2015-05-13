from KettleStep import KettleStep

__author__ = 'aoverton'


class FtbImportV1(KettleStep):
    """
    Modesl the FTBImportPluginV1 step. Relies heavily on members created in parent class
    """

    step_name = 'FTBImportPluginV1'

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.existence(self.NOTIFICATION, self.issue_messages.ftb_importv1)
        return self.issues
