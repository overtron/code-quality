import unittest

from git.kettle_validation.classes.ExcelInputTrans import ExcelInput
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
            <name>Microsoft Excel Input</name>
            <type>ExcelInput</type>
            <limit>1</limit>
            <encoding/>
            <file>
              <file_required>N</file_required>
            </file>
            </step>
        </transformation>'''

    def setUp(self):
        self.data = ParseKettleXml(self.data, isFile=False).parse_xml()

    def test_run_tests(self):
        t = ExcelInput(self.data)
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(1, len(result['warnings']), "Required File")
        self.assertEqual(2, len(result['errors']), "File Encoding, Limit Field")


if __name__ == '__main__':
    unittest.main()
