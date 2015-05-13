import os

__author__ = 'aoverton'

__all__ = []
for file_name in os.listdir(os.path.dirname(__file__)):
    if file_name.endswith("Trans.py"):  # all transformation checks must end with Trans.py
        short_file_name = file_name[:-3]  # removes .py
        __all__.append(short_file_name)
class_list_trans = __all__


