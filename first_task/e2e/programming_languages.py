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

    def map(raw_data: [str]):
        if not raw_data:
            raise ValueError("Could not map because input list was empty")
        return ProgrammingLanguages(website=raw_data[0], 
                                    popularity=raw_data[1], 
                                    frontend=raw_data[2],
                                    backend=raw_data[3],
                                    database=raw_data[4],
                                    notes=raw_data[5])
    
    def _parse(self, input: str) -> int:
        return int(re.sub(r'[^\d]', '', input))
    
    def _extract_payload(self, input: str):
        return re.sub(r'\[.*?\]|\(.*?\)', '', input)