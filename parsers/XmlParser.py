import json
import xml.etree.ElementTree as et
import xmltodict, json


class XmlParser:
    def __init__(self, urls):
        self.urls = urls

    def to_json(self):
        for _ , url in enumerate(self.urls):
            with open(url) as xml:
                data = xmltodict.parse(xml.read())

            data['file_name'] = url

            with open(f'output/output-{((url.split("/"))[-1]).split(".")[0]}.json', 'w+') as f:
                json.dump(data, f)

