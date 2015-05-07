
__author__ = 'aoverton'

WARNING = 'warning'
ERROR = 'error'
CONVENTION = 'convention'

class PrettyColors(object):
    colors = {
        'red': '\033[1;31m',
        'green': '\033[1;32m',
        'yellow': '\033[1;33m',
        'cyan': '\033[0;36m',
        'off': '\033[0m'
    }

    def colorize(self, text, color):
        return self.colors[color] + text + self.colors['off']

    def red(self, text):
        return self.colorize(text, 'red')

    def cyan(self, text):
        return self.colorize(text, 'cyan')

    def green(self, text):
        return self.colorize(text, 'green')

    def yellow(self, text):
        return self.colorize(text, 'yellow')

    def format(self, text, issue_type):
        """
        :param text: the text you want to print
        :param issue_type: the type of issue (warning, error, convention)
        :return: the colored text
        """
        if issue_type == WARNING:
            return self.yellow(text)
        elif issue_type == ERROR:
            return self.red(text)
        elif issue_type == CONVENTION:
            return self.cyan(text)
        else:
            return text
