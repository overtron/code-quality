import os

from custom_exceptions import FileNotFound, InvalidFileType


__author__ = 'aoverton'


def get_files_from_path(path, endings_list):
    files = []
    if not os.path.exists(path):
        raise FileNotFound
    if os.path.isfile(path):
        valid_ending = False
        for ending in endings_list:
            if path.endswith(ending):
                files.append(path)
                valid_ending = True
        if not valid_ending:
            raise InvalidFileType
    elif os.path.isdir(path):
        for this_path, _, these_files in os.walk(path):
            for this_file in these_files:
                for ending in endings_list:
                    if this_file.endswith(ending):
                        files.append(os.path.join(this_path, this_file))
    if not files:
        raise FileNotFound
    else:
        return files