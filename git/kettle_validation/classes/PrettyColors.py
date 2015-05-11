
__author__ = 'aoverton'

WARNING = 'warning'
ERROR = 'error'
CONVENTION = 'convention'

class PrettyColors(object):
    """
    Class to print colored text to the terminal window using ANSI escape codes

    """
    colors = {
        'red': '\033[1;31m',
        'green': '\033[1;32m',
        'yellow': '\033[1;33m',
        'cyan': '\033[0;36m',
        'off': '\033[0m'
    }

    def colorize(self, text, color):
        """
        Return the text string colored to the chosen color. Color choice must appear in colors dict

        :param text: text to color
        :param color: color choice
        :return: string with ANSI escape codes prepended and appended
        """
        return self.colors[color] + text + self.colors['off']

    def red(self, text):
        """
        Color text red

        :param text:  text to color
        :return: text string with red ANSI escape codes
        """
        return self.colorize(text, 'red')

    def cyan(self, text):
        """
        Color text cyan

        :param text:  text to color
        :return: text string with cyan ANSI escape codes
        """
        return self.colorize(text, 'cyan')

    def green(self, text):
        """
        Color text green

        :param text:  text to color
        :return: text string with green ANSI escape codes
        """
        return self.colorize(text, 'green')

    def yellow(self, text):
        """
        Color text yellow

        :param text:  text to color
        :return: text string with yellow ANSI escape codes
        """
        return self.colorize(text, 'yellow')

    def format(self, text, issue_type):
        """
        Returns text formatted in the appropriate color depending on what type of issue it is

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
