import unittest

from git.kettle_validation.classes.TableOutputTrans import TableOutput
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
            <name>Table output</name>
            <type>TableOutput</type>
            <ignore_errors>Y</ignore_errors>
            </step>
        </transformation>'''

    def setUp(self):
        self.data = ParseKettleXml(self.data, isFile=False).parse_xml()

    def test_run_tests(self):
        t = TableOutput(self.data['steps'][TableOutput.step_name])
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(1, len(result['warnings']), "Ignore Insert Errors")
        self.assertEqual(0, len(result['errors']), "No Errors Should be Thrown")


if __name__ == '__main__':
    unittest.main()
