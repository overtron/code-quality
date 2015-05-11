from KettleStep import KettleStep

__author__ = 'aoverton'


class GeneralTransformation(KettleStep):
    """
    Models trans features that are not specific to a given step. Relies heavily on members created in parent class

    """

    def __init__(self, data):
        """
        Call parent init and select relevant steps

        :param data: dict of step names and corresponding list of steps from trans/job
        :return: None
        """
        KettleStep.__init__(self)
        self.data = data

    def add_hops(self, hops, issue_t, message):
        """
        Add hops that have issues to the issue tracker

        :param hops: hops that have issues
        :param issue_t: type of issue
        :param message: message to log for the issue
        :return: None
        """
        make_name = lambda x,y: "{} -> {}".format(x, y)
        for hop in hops:
            from_name = hop.find("from").text
            to_name = hop.find("to").text
            self.add_issue(issue_t, self.Issue(make_name(from_name, to_name), message))

    def disabled_hops(self):
        """
        Check for disabled hops

        :return: None
        """
        disabled_hops = []
        for hop in self.data['hops']:
            if hop.find("enabled").text.lower() == "y":
                disabled_hops.append(hop)
        self.add_hops(disabled_hops, self.ERRORS, self.issue_messages.disabled_hops)

    def add_handlers(self, handlers, issue_t, message):
        """
        Add error handlers that have issues to the issue tracker

        :param handlers: handlers that have issues
        :param issue_t:  type of issue
        :param message: message to log for the issue
        :return: None
        """
        for handle in handlers:
            self.add_issue(issue_t, self.Issue(handle.find("source_step").text, message))

    def error_handling(self):
        """
        Check if error handling is turned on without a target step to receive the errors

        :return: None
        """
        hidden_error_handlers = []
        for handler in self.data['error_handling']:
            if handler.find("is_enabled").text.lower() == "y" and handler.find("target_step").text in ["", None]:
                hidden_error_handlers.append(handler)
        self.add_handlers(hidden_error_handlers, self.ERRORS, self.issue_messages.hidden_error_handlers)

    def run_tests(self):
        """
        Run all tests in class

        :return: issues from test
        """
        self.disabled_hops()
        self.error_handling()
        return self.issues
