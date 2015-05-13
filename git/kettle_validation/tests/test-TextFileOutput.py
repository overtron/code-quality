import unittest

from git.kettle_validation.classes.TextFileOutputTrans import TextFileOutput
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
            <name>Text file output</name>
            <type>TextFileOutput</type>
            <encoding>MacRoman</encoding>
            </step>
        </transformation>'''

    def setUp(self):
        self.data = ParseKettleXml(self.data, isFile=False).parse_xml()

    def test_run_tests(self):
        t = TextFileOutput(self.data)
        t = TextFileOutput(self.data['steps'][TextFileOutput.step_name])
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(0, len(result['warnings']), "No warnings should be returned")
        self.assertEqual(1, len(result['errors']), "UTF-8 Encoding")


if __name__ == '__main__':
    unittest.main()
