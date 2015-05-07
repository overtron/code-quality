import unittest

from git.kettle_validation.classes.SortRowsTrans import SortRows
from git.kettle_validation.tests.pretty_print import pretty_print
from git.kettle_validation.parse_kettle_xml import ParseKettleXml

__author__ = 'aoverton'


class MyTestCase(unittest.TestCase):
    data = '''<?xml version="1.0" encoding="UTF-8"?>
        <transformation>
          <info>
            <name>Test</name>
          </info>
          <step>
            <name>Sort rows</name>
            <type>SortRows</type>
            <unique_rows>Y</unique_rows>
          </step>
        </transformation>'''

    def setUp(self):
        self.data = ParseKettleXml(self.data, isFile=False).parse_xml()

    def test_run_tests(self):
        t = SortRows(self.data)
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(1, len(result['warnings']), "Unique Option")
        self.assertEqual(0, len(result['errors']), "No Errors")


if __name__ == '__main__':
    unittest.main()
