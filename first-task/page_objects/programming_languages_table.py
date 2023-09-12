from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from programming_languages import ProgrammingLanguages

class ProgrammingLanguagesTable(WebElement):
    
    def __init__(self, element: WebElement):
        self.element = element
        self.caption = element.find_element(By.TAG_NAME, 'caption')
        self.table_rows = element.find_elements(By.TAG_NAME, 'tr')

    def map_table_data(self) -> list[ProgrammingLanguages]:
        table_data = []
        for row in self.table_rows:
            if not self._map_row(row):
                continue
            table_data.append(self._map_row(row))
        return table_data

    def _map_row(self, row: WebElement) -> ProgrammingLanguages:
        data_from_row = self._get_data_from_row(row)
        if not data_from_row:
            return
        return ProgrammingLanguages(website=data_from_row[0], 
                                    popularity=data_from_row[1], 
                                    frontend=data_from_row[2],
                                    backend=data_from_row[3],
                                    database=data_from_row[4],
                                    notes=data_from_row[5])
    
    def _get_data_from_row(self, row: WebElement):
        cells = row.find_elements(By.TAG_NAME, 'td')
        row_data = [cell.text for cell in cells]
        return row_data