import unittest

from git.kettle_validation.classes.TableInputTrans import TableInput
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
            <name>Table input</name>
            <type>TableInput</type>
            <sql>SELECT &#x2a; FROM &#x3c;table name&#x3e; WHERE &#x3c;conditions&#x3e;</sql>
            <limit>150</limit>
            <lazy_conversion_active>Y</lazy_conversion_active>
            </step>
        </transformation>'''

    def setUp(self):
        self.data = ParseKettleXml(self.data, isFile=False).parse_xml()

    def test_run_tests(self):
        t = TableInput(self.data)
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(2, len(result['warnings']), "Select *, Lazy Conversion")
        self.assertEqual(1, len(result['errors']), "Limit")


if __name__ == '__main__':
    unittest.main()
