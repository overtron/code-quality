import xml.etree.ElementTree as ET
import logging
from collections import defaultdict

__author__ = 'aoverton'


class ParseKettleXml:
    """
    Parses kettle .ktr and .kjb files for easy manipulation by other tools

    """
    def __init__(self, data, isFile=True):
        """
        Create object for kettle parsing

        :param data: File pointer or string of kettle XML
        :param isFile: Flag that indicates whether or not a file point or string is being passed
        :return: None
        """
        self.logger = logging.getLogger()
        self.root = None
        self.steps = defaultdict(list)
        self.hops = []
        self.error_handling = []
        self.data = data
        self.isFile = isFile
        self.name = ""

    def parse_xml(self):
        """
        Coordinates parsing of XML to its component pieces

        :return: dict that contains key parts of XML extracted
        """
        if self.isFile:
            self.root = ET.parse(self.data).getroot()
        else:
            self.root = ET.fromstring(self.data)
        self.parse_elements()
        return {'steps': self.steps,
                'hops': self.hops,
                'error_handling': self.error_handling,
                'name': self.name}

    def parse_elements(self):
        """
        Finds and extracts the relevant parts of the XML based on whether it is a trans or job

        :return: None
        """
        if self.root.tag == "transformation":
            self.name = self.root.find("./info/name").text
            for step in self.root.iter("step"):
                try:
                    self.steps[step.find("type").text].append(step)
                except AttributeError:
                    pass
            for hop in self.root.iter("hop"):
                self.hops.append(hop)
            for error_node in self.root.iter("error"):
                self.error_handling.append(error_node)
        elif self.root.tag == "job":
            self.name = self.root.find("./name").text
            for step in self.root.iter("entry"):
                self.steps[step.find("type").text].append(step)
            for hop in self.root.iter("hop"):
                self.hops.append(hop)
        else:
            self.logger("Invalid XML. Root tag should be 'transformation' or 'job'")
            raise ValueError



