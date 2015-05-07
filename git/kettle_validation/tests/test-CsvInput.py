import unittest

from git.kettle_validation.classes.CsvInputTrans import CsvInput
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
        <name>CSV file input</name>
        <type>CsvInput</type>
        <lazy_conversion>Y</lazy_conversion>
        <encoding/>
        </step>
    </transformation>'''

    def setUp(self):
        self.data = ParseKettleXml(self.data, isFile=False).parse_xml()

    def test_run_tests(self):
        t = CsvInput(self.data)
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(1, len(result['warnings']), "Lazy Conversion")
        self.assertEqual(1, len(result['errors']), "File Encoding")


if __name__ == '__main__':
    unittest.main()
