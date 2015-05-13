from KettleStep import KettleStep

__author__ = 'aoverton'


class FtbImportV0(KettleStep):
    """
    Models the FTBImportPlugin step. Relies heavily on members created in parent class

    """

    step_name = 'FTBImportPlugin'

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.existence(self.NOTIFICATION, self.issue_messages.ftb_importv0)
        return self.issues
