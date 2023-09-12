from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.programming_languages_table import ProgrammingLanguagesTable

class ProgrammingLanguagesPage():

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.programming_languages_table = ProgrammingLanguagesTable(self.driver.find_element(By.CLASS_NAME, 'wikitable'))

    def get_table_data(self):
        self._wait_page_loaded()
        return self.programming_languages_table.map_table_data()

    def _wait_page_loaded(self, timeout = 10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1#firstHeading span")))
            print('Element title found on page')
        except:
            print(f'Timed out waiting for an element title on page {timeout} sec')