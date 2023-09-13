import re

class ProgrammingLanguages():
    
    def __init__(self,
                 website: str,
                 popularity: str,
                 frontend: str,
                 backend: str,
                 database: str,
                 notes: str):
        self.website = self._extract_payload(website)
        self.popularity = self._parse(popularity)
        self.frontend = self._extract_payload(frontend)
        self.backend = self._extract_payload(backend)
        self.database = self._extract_payload(database)
        self.notes = notes

    def _parse(self, input: str) -> int:
        return int(re.sub(r'[^\d]', '', input))
    
    def _extract_payload(self, input: str):
        return re.sub(r'\[.*?\]|\(.*?\)', '', input)