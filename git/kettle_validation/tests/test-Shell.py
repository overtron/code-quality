import unittest

from git.kettle_validation.classes.ShellJob import Shell
from git.kettle_validation.classes.IssueMessages import IssueMessages
from git.kettle_validation.tests.pretty_print import pretty_print
from git.kettle_validation.parse_kettle_xml import ParseKettleXml

__author__ = 'aoverton'


class MyTestCase(unittest.TestCase):

    messages = IssueMessages()

    def test_run_tests_dl_found(self):
        data = '''<?xml version="1.0" encoding="UTF-8"?>
        <job>
          <name>all-job-steps</name>
          <entries>
            <entry>
              <name>Data Logistics</name>
              <type>SHELL</type>
              <insertScript>Y</insertScript>
              <script>&#x2f;opt&#x2f;devops&#x2f;datalogistics&#x2f;2.0&#x2f;table_copy -o db5 -d workhorse1b -od
              app_db_5 -dd app_db_5 -t test_table&#xa;&#x2f;opt&#x2f;devops&#x2f;datalogistics&#x2f;table_copy -o db5
              -d workhorse1b -od app_db_5 -dd app_db_5 -t test_table&#xa;&#x2f;opt&#x2f;devops&#x2f;etl_impexp&#x2f;
              etl2prod.py&#xa;&#x2f;opt&#x2f;devops&#x2f;etl_impexp&#x2f;prod2etl.py&#xa;</script>
              </entry>
          </entries>
          <hops>
          </hops>
          <notepads>
          </notepads>
        </job>
        '''
        data = ParseKettleXml(data, isFile=False).parse_xml()
        t = Shell(data['steps'][Shell.step_name])
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(self.messages.data_logistics, result['notifications'][0].message, "Data Logistics used")
        self.assertEqual(self.messages.deprecated_dl, result['notifications'][1].message, "Deprecated DL used")

    def test_run_tests_dl_possible(self):
        data = '''<?xml version="1.0" encoding="UTF-8"?>
        <job>
          <name>all-job-steps</name>
          <entries>
            <entry>
              <name>Data Logistics</name>
              <type>SHELL</type>
              <insertScript>N</insertScript>
              <script>&#x2f;opt&#x2f;devops&#x2f;datalogistics&#x2f;2.0&#x2f;table_copy -o db5 -d workhorse1b -od
              app_db_5 -dd app_db_5 -t test_table&#xa;&#x2f;opt&#x2f;devops&#x2f;datalogistics&#x2f;table_copy -o db5
              -d workhorse1b -od app_db_5 -dd app_db_5 -t test_table&#xa;&#x2f;opt&#x2f;devops&#x2f;etl_impexp&#x2f;
              etl2prod.py&#xa;&#x2f;opt&#x2f;devops&#x2f;etl_impexp&#x2f;prod2etl.py&#xa;</script>
              </entry>
          </entries>
          <hops>
          </hops>
          <notepads>
          </notepads>
        </job>
        '''
        data = ParseKettleXml(data, isFile=False).parse_xml()
        t = Shell(data['steps'][Shell.step_name])
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(self.messages.external_script, result['notifications'][0].message, "Data Logistics Possible")

    def test_table_copy(self):
        data = '''<?xml version="1.0" encoding="UTF-8"?>
        <job>
          <name>all-job-steps</name>
          <entries>
            <entry>
              <name>Data Logistics</name>
              <type>SHELL</type>
              <insertScript>Y</insertScript>
              <script>&#x2f;opt&#x2f;devops&#x2f;datalogistics&#x2f;2.0&#x2f;table_copy -o db5 -d workhorse1b -od
              app_db_5 -dd app_db_5 -t test_table</script>
              </entry>
          </entries>
          <hops>
          </hops>
          <notepads>
          </notepads>
        </job>
        '''
        data = ParseKettleXml(data, isFile=False).parse_xml()
        t = Shell(data['steps'][Shell.step_name])
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(self.messages.data_logistics, result['notifications'][0].message, "Table Copy")

    def test_etl2prod(self):
        data = '''<?xml version="1.0" encoding="UTF-8"?>
        <job>
          <name>all-job-steps</name>
          <entries>
            <entry>
              <name>Data Logistics</name>
              <type>SHELL</type>
              <insertScript>Y</insertScript>
              <script>&#xa;&#x2f;opt&#x2f;devops&#x2f;etl_impexp&#x2f;etl2prod.py</script>
              </entry>
          </entries>
          <hops>
          </hops>
          <notepads>
          </notepads>
        </job>
        '''
        data = ParseKettleXml(data, isFile=False).parse_xml()
        t = Shell(data['steps'][Shell.step_name])
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(self.messages.deprecated_dl, result['notifications'][0].message, "etl2prod")

    def test_prod2etl(self):
        data = '''<?xml version="1.0" encoding="UTF-8"?>
        <job>
          <name>all-job-steps</name>
          <entries>
            <entry>
              <name>Data Logistics</name>
              <type>SHELL</type>
              <insertScript>Y</insertScript>
              <script>&#xa;&#x2f;opt&#x2f;devops&#x2f;etl_impexp&#x2f;prod2etl.py&#xa;</script>
              </entry>
          </entries>
          <hops>
          </hops>
          <notepads>
          </notepads>
        </job>
        '''
        data = ParseKettleXml(data, isFile=False).parse_xml()
        t = Shell(data['steps'][Shell.step_name])
        result = t.run_tests()
        pretty_print(result)
        self.assertEqual(self.messages.deprecated_dl, result['notifications'][0].message, "prod2etl")


if __name__ == '__main__':
    unittest.main()
