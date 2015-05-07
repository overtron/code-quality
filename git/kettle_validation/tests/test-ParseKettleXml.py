import unittest

from git.kettle_validation.parse_kettle_xml import ParseKettleXml


__author__ = 'aoverton'


class MyTestCase(unittest.TestCase):

    def test_job_string(self):
        data = '''<?xml version="1.0" encoding="UTF-8"?>
        <job>
          <name>update-unemployment-rates</name>
          <entries>
            <entry>
              <name>START</name>
              <type>MAIL</type>
            </entry>
            <entry>
              <name>Pull Data from BLS API</name>
              <type>SHELL</type>
            </entry>
            <entry>
              <name>Generate Insights</name>
              <type>SHELL</type>
            </entry>
            <entry>
              <name>Clean Data</name>
              <type>SHELL</type>
            </entry>
            <entry>
              <name>Modify Data for Geo Updates</name>
              <type>SHELL</type>
            </entry>
          </entries>
          <hops>
            <hop>
              <from>START</from>
              <to>Pull Data from BLS API</to>
            </hop>
            <hop>
              <from>Clean Data</from>
              <to>Generate Insights</to>
            </hop>
            <hop>
              <from>Generate Insights</from>
              <to>Update US Unemployment Rates</to>
            </hop>
            <hop>
              <from>Modify Data for Geo Updates</from>
              <to>Update Geo Unemployment Rates</to>
            </hop>
            <hop>
              <from>Update US Unemployment Rates</from>
              <to>Modify Data for Geo Updates</to>
            </hop>
          </hops>
        </job>'''
        t = ParseKettleXml(data, isFile=False)
        results = t.parse_xml()
        self.assertEqual(2, len(results['steps'].items()), "Step Key")
        self.assertEqual(4, len(results['steps']['SHELL']), "Step Value")
        self.assertEqual(5, len(results['hops']), "Hops")

    def test_transformation_string(self):
        data = '''<?xml version="1.0" encoding="UTF-8"?>
        <transformation>
          <info>
            <name>all-steps</name>
          </info>
          <order>
            <hop>
              <from>Take in Unemployment Data</from>
              <to>CSV file input</to>
              <enabled>Y</enabled>
            </hop>
            <hop>
              <from>CSV file input</from>
              <to>Microsoft Excel Input</to>
              <enabled>N</enabled>
            </hop>
          </order>
          <step>
            <type>JsonInput</type>
          </step>
          <step>
            <type>CsvInput</type>
          </step>
          <step>
            <type>JsonInput</type>
          </step>
          <step>
            <type>JsonInput</type>
          </step>
        </transformation>'''
        t = ParseKettleXml(data, isFile=False)
        results = t.parse_xml()
        self.assertEqual(2, len(results['steps'].items()), "Step Key")
        self.assertEqual(3, len(results['steps']['JsonInput']), "Step Value")
        self.assertEqual(2, len(results['hops']), "Hops")


if __name__ == '__main__':
    unittest.main()
