import os

from custom_exceptions import FileNotFound, InvalidFileType


__author__ = 'aoverton'


def get_files_from_path(path, endings_list):
    """
    Extracts the valid file(s) from a file or folder

    :param path: path to target file or folder
    :param endings_list: list of valid endings
    :return: list of valid files
    """
    files = []
    if not os.path.exists(path):
        raise FileNotFound("Path does not exist. Please ensure you are passing a valid file or folder.")
    if os.path.isfile(path):
        for ending in endings_list:
            if path.endswith(ending):
                return [path]
        raise InvalidFileType("File provided does not have a valid ending.")
    elif os.path.isdir(path):
        for this_path, _, these_files in os.walk(path):
            for this_file in these_files:
                for ending in endings_list:
                    if this_file.endswith(ending):
                        files.append(os.path.join(this_path, this_file))
    if not files:
        raise FileNotFound("No valid files were found to work with.")
    else:
        return files