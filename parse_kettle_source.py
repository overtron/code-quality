'''
Created on Apr 6, 2015

@author: nnair

Python script to parse Kettle files and validate it against set standards
'''

import re
import sys
import logging
import argparse
import xml.etree.ElementTree as ET
from names_regex import DEFAULT_NAMES as DEFAULT_NAMES

# --------------------------------------------------------------------------------------------------

PARSER_LOGGER = logging.getLogger(__name__)
logging.addLevelName(logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))

# --------------------------------------------------------------------------------------------------


def step_notes(root):
    """
    Find all notes in the root element of kettle file
    If there are no notes, fail
    :param root:
    """
    PARSER_LOGGER.info('Checking for notes')
    step_notes_passed = True
    notepads = root.findall('./notepads/notepad/note')
    if not notepads:
        step_notes_passed = False
    return step_notes_passed

# --------------------------------------------------------------------------------------------------


def evaluate_entries(entries):
    """
    If any name is the same as the default name return false
    :param entries:
    """
    step_names_passed = True
    evaluated = False
    for entryname in entries:
        PARSER_LOGGER.info('Checking entry {}'.format(entryname.text))
        for default_name in DEFAULT_NAMES:
            if re.findall(default_name, entryname.text):
                step_names_passed = False
                evaluated = True
                break
        if evaluated:
            break
    return step_names_passed

# --------------------------------------------------------------------------------------------------


def step_names(root):
    """
    Find all entries in root element
    check if they have non default names
    :param root:
    """
    PARSER_LOGGER.info('Checking Step Names')
    type = root.tag
    if type == "job":
        entries = root.findall('./entries/entry/name')
    elif type == "transformation":
        entries = root.findall('./step/name')

    step_names_passed = evaluate_entries(entries)

    return step_names_passed

# --------------------------------------------------------------------------------------------------


def evaluate_descriptions(entries):
    """
    If no description text fail check
    :param entries:
    """
    step_descriptions_passed = True
    for entrydesc in entries:
        if not entrydesc.text:
            step_descriptions_passed = False

    return step_descriptions_passed

# --------------------------------------------------------------------------------------------------


def step_descriptions(root):
    """
    Takes root element and finds descriptions
    If no descriptions exist for each entry - return False
    :param root:
    :returntype boolean:
    """
    PARSER_LOGGER.info('Checking descriptions')
    type = root.tag
    if type == "job":
        entries = root.findall('./entries/entry/description')
    else:
        entries = root.findall('./step/description')

    step_descriptions_passed = evaluate_descriptions(entries)
    return step_descriptions_passed

# --------------------------------------------------------------------------------------------------


def kettle_evaluate(root):
    evaluation_passed = True
    if step_names(root):
        PARSER_LOGGER.info('Step names check passed')
    else:
        PARSER_LOGGER.error('Step names checks failed')
    if step_descriptions(root):
        PARSER_LOGGER.info('Step descriptions check passed')
    else:
        PARSER_LOGGER.error('Step descriptions check failed')

    if step_notes(root):
        PARSER_LOGGER.info('Notes check passed')
    else:
        PARSER_LOGGER.error('Notes check failed')
    return evaluation_passed

# --------------------------------------------------------------------------------------------------


def parse_command_line_args():
    parser = argparse.ArgumentParser(
        description='Parse the Kettle file evaluate against kettle standards')
    parser.add_argument('--filename', '-f', type=str, help='filename of the file to evaluate')

    return parser.parse_args()

# --------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    PARSER_LOGGER = logging.getLogger()
    PARSER_LOGGER.setLevel(logging.INFO)
    CONSOLE_HANDLER = logging.StreamHandler(sys.stdout)
    CONSOLE_HANDLER.setLevel(logging.INFO)
    CONSOLE_HANDLER.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    PARSER_LOGGER.addHandler(CONSOLE_HANDLER)

    CL_ARGS = parse_command_line_args()
    FILENAME = CL_ARGS.filename
    TREE = ET.parse(FILENAME)
    ROOT = TREE.getroot()
    kettle_evaluate(ROOT)
