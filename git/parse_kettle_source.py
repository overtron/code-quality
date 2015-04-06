'''
Created on Apr 6, 2015

@author: nnair

Python script to parse Kettle files and validate it against set standards
'''

import re
import xml.etree.ElementTree as ET

# --------------------------------------------------------------------------------------------------

# TODO: Complete default name list
_RE_DEFAULT_JOB_NAME = re.compile('^Job', re.IGNORECASE)
_RE_DEFAULT_TRANS_NAME = re.compile('^Transformation', re.IGNORECASE)
DEFAULT_NAMES = [_RE_DEFAULT_JOB_NAME, _RE_DEFAULT_TRANS_NAME]

# --------------------------------------------------------------------------------------------------


def step_notes(root):
    """
    Find all notes in the root element of kettle file
    If there are no notes, fail
    :param root:
    """
    step_notes_passed = True
    notepads = root.findall('./notepads/notepad/note')
    if not notepads:
        step_notes_passed = False
    return step_notes_passed

# --------------------------------------------------------------------------------------------------


def step_names(root):
    """
    Find all entries in root element
    check if they have non default names
    :param root:
    """
    step_names_passed = True
    entries = root.findall('./entries/entry/name')
    for entryname in entries:
        for default_name in DEFAULT_NAMES:
            if re.findall(default_name, entryname.text):
                step_names_passed = False
    return step_names_passed

# --------------------------------------------------------------------------------------------------


def step_descriptions(root):
    """
    Takes root element and finds descriptions
    If no descriptions exit for each entry - return False
    TODO:
    method throws - Handle
    __main__:11: FutureWarning: The behavior of this method will change in future versions.
    Use specific 'len(elem)' or 'elem is not None' test instead.
    :param root:
    :returntype boolean:
    """
    step_descriptions_passed = True
    entries = root.findall('./entries/entry/description')
    for entrydesc in entries:
        if not entrydesc:
            step_descriptions_passed = False
    return step_descriptions_passed

# --------------------------------------------------------------------------------------------------


def kettle_evaluate(root):
    step_names(root)
    step_descriptions(root)
    return

# --------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    """
    Change filename to test
    """
    TREE = ET.parse('/Users/nnair/Downloads/copyforpm/form_d_companies.kjb')
    ROOT = TREE.getroot()
    kettle_evaluate(ROOT)
