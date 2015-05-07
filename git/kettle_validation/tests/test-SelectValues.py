import unittest

from git.kettle_validation.classes.SelectValuesTrans import SelectValues
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
            <name>Select values</name>
            <type>SelectValues</type>
            <fields>
              <field>
                <name>test</name>
                <rename/>
                <length>-2</length>
                <precision>-2</precision>
              </field>
              <select_unspecified>N</select_unspecified>
              <remove>
                <name>test2</name>
              </remove>
              <meta>
                <name>test3</name>
                <rename>test3</rename>
                <type>None</type>
                <length>-2</length>
                <precision>-2</precision>
                <conversion_mask/>
                <date_format_lenient>false</date_format_lenient>
                <date_format_locale/>
                <date_format_timezone/>
                <lenient_string_to_number>false</lenient_string_to_number>
                <encoding/>
                <decimal_symbol/>
                <grouping_symbol/>
                <currency_symbol/>
                <storage_type/>
              </meta>
            </fields>
          </step>
        </transformation>'''

    def setUp(self):
        self.data = ParseKettleXml(self.data, isFile=False).parse_xml()

    def test_run_tests(self):
        t = SelectValues(self.data)
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(0, len(result['warnings']), "No Warnings")
        self.assertEqual(1, len(result['errors']), "Multiple Tabs")


if __name__ == '__main__':
    unittest.main()
