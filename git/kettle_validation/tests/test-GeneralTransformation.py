import unittest

from git.kettle_validation.classes.GeneralTransformationTrans import GeneralTransformation
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
            <hop>
              <from>CSV file input</from>
              <to>Microsoft Excel Input</to>
              <enabled>Y</enabled>
            </hop>
          </order>
          <step_error_handling>
              <error>
                <source_step>Table output</source_step>
                <target_step/>
                <is_enabled>Y</is_enabled>
              </error>
          </step_error_handling>
        </transformation>'''

    def setUp(self):
        self.data = ParseKettleXml(self.data, isFile=False).parse_xml()

    def test_run_tests(self):
        t = GeneralTransformation(self.data)
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(0, len(result['warnings']), "No warnings")
        self.assertEqual(2, len(result['errors']), "Disabled Hops, Hidden Error Handling")


if __name__ == '__main__':
    unittest.main()
