from typing import List


class Item(object):

    def __init__(self, title: str, desc: str, cover: str, pdf: str) -> None:
        super().__init__()

        self.title = title
        self.desc = desc
        self.cover = cover
        self.pdf = pdf


class Section(object):

    def __init__(self, id: str, name: str, url: str, items: List[Item]) -> None:
        super().__init__()

        self.id = id
        self.name = name
        self.url = url
        self.items = items
