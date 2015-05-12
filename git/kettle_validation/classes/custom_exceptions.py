
__author__ = 'aoverton'


class InvalidIssueType(Exception):
    """
    Exception to be thrown when an invalid issue type is used

    """
    pass


class FileNotFound(Exception):
    """
    Exception to be thrown when a valid file cannot be found

    """
    pass


class InvalidFileType(Exception):
    """
    Exception to be thrown when a given file has an invalid ending

    """
    pass