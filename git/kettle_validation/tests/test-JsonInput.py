import unittest

from git.kettle_validation.classes.JsonInputTrans import JsonInput
from git.kettle_validation.tests.pretty_print import pretty_print
from git.kettle_validation.parse_kettle_xml import ParseKettleXml

__author__ = 'aoverton'


class MyTestCase(unittest.TestCase):
    data = '''<?xml version="1.0" encoding="UTF-8"?>
        <transformation>
          <info>
            <name>Test</name>
          </info>
          <order>
              <hop> <from>Add constants</from><to>Stream lookup</to><enabled>Y</enabled> </hop>
          </order>
          <step>
            <name>Json Input</name>
            <type>JsonInput</type>
            <IsIgnoreEmptyFile>Y</IsIgnoreEmptyFile>
            <doNotFailIfNoFile>Y</doNotFailIfNoFile>
            <file>
              <file_required>N</file_required>
            </file>
            <limit>1987</limit>
            </step>
        </transformation>'''

    def setUp(self):
        self.data = ParseKettleXml(self.data, isFile=False).parse_xml()

    def test_run_tests(self):
        t = JsonInput(self.data)
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(3, len(result['warnings']), "Required File, Ignore Empty File, Ignore Missing File")
        self.assertEqual(1, len(result['errors']), "Limit")


if __name__ == '__main__':
    unittest.main()
