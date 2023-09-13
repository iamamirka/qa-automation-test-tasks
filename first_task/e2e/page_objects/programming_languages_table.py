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
        return ProgrammingLanguages.map(data_from_row)
    
    def _get_data_from_row(self, row: WebElement) -> [str]:
        cells = row.find_elements(By.TAG_NAME, 'td')
        row_data = [cell.text for cell in cells]
        return row_data