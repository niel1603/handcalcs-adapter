from utils.sections.enum import SectionKey, SourceKey

class SectionRegistry:
    def __init__(self):
        self._tables = {}

    def _ensure_loaded(self, source: SourceKey):
        if source in self._tables:
            return

        info = source.value
        self._tables[source] = info.loader(info.path, info.standard)

    def get(self, key: SectionKey, source: SourceKey):
        self._ensure_loaded(source)
        return self._tables[source][key.key]

