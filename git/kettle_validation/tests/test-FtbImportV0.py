import unittest

from git.kettle_validation.classes.FtbImportV0Trans import FtbImportV0
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
            <name>FindTheBest Import</name>
            <type>FTBImportPlugin</type>
            </step>
        </transformation>'''

    def setUp(self):
        self.data = ParseKettleXml(self.data, isFile=False).parse_xml()

    def test_run_tests(self):
        t = FtbImportV0(self.data['steps'][FtbImportV0.step_name])
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(1, len(result['notifications']), "Ftb Import V0 Existence")


if __name__ == '__main__':
    unittest.main()
