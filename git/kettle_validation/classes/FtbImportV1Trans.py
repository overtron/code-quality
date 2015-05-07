from KettleStep import KettleStep

__author__ = 'aoverton'


class FtbImportV1(KettleStep):
    def __init__(self, data):
        KettleStep.__init__(self)
        self.all_steps = data['steps']['FTBImportPluginV1']

    def existence(self):
        self.add_all_issues(self.all_steps, self.NOTIFICATION, self.issue_messages.ftb_importv1)

    def run_tests(self):
        self.existence()
        return self.issues
