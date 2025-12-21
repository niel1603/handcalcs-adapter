# sections/table.py
class SectionTable:
    def __init__(self, standard: str):
        self.standard = standard
        self._items = {}

    def add(self, section):
        if section.name in self._items:
            raise KeyError(f"Duplicate section: {section.name}")
        self._items[section.name] = section

    def get(self, name):
        return self._items[name]

    def has(self, name):
        return name in self._items

    def all(self):
        return list(self._items.values())
