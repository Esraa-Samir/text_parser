from parsers.XmlParser import XmlParser
from parsers.CsvParser import CsvParser

class ObjectParser:
    def parse(self, url, format):
        parser = factory.get_parser(format, url)
        return parser.to_json()


class ParserFactory:
    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_parser(self, format, url):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator(url)


factory = ParserFactory()
factory.register_format('XML', XmlParser)
factory.register_format('CSV', CsvParser)