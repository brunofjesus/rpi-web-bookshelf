from xml.etree.ElementTree import fromstring, ElementTree, Element
import requests

from bookshelf import config
from bookshelf.model import Section, Item


class Parser(object):

    def parse_sections(self):
        f = open(config.XML_FILENAME, 'r')

        tree = ElementTree(fromstring(f.read()))

        f.close()
        root = tree.getroot()

        result = []

        for element_section in root:
            name = element_section.find(config.SECTION_NAME).text.replace("_", "")
            url = element_section.find(config.SECTION_URL).text
            items = element_section.find(config.SECTION_ITEM)
            if items is not None:
                result.append(
                    Section(element_section.tag, name, url, self.__parse_items(element_section))
                )

        return result

    @staticmethod
    def __parse_items(element: Element):
        result = []
        element_item_list = element.findall(config.SECTION_ITEM)

        for element_item in element_item_list:
            title = element_item.find(config.ITEM_TITLE).text
            desc = element_item.find(config.ITEM_DESCRIPTION).text
            cover = element_item.find(config.ITEM_COVER_URL).text
            pdf = element_item.find(config.ITEM_PDF_URL).text

            result.append(
                Item(title, desc, cover, pdf)
            )

        return result

    @staticmethod
    def fetch():
        http_response = requests.get(config.XML_URL)
        f = open(config.XML_FILENAME, 'wb')
        f.write(http_response.content)
        f.close()


if __name__ == "__main__":
    Parser.fetch()

    p = Parser()
    sections = p.parse_sections()

    for sect in sections:
        print("{} - {} - {}".format(sect.name, sect.url, len(sect.items)))
        for item in sect.items:
            print("\t== {} ==\n\t\t{}\n\t\t{}".format(item.title, item.desc, item.pdf))
