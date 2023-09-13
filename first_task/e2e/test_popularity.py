import pytest
from selenium import webdriver
from data.programming_languages import ProgrammingLanguages
from navigation.wiki_navigation import WikiNavigation

class TestPopularity():
    
    expected_cases = [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 1.5 * 10**9]

    @pytest.mark.parametrize("expected", expected_cases)
    def test_website_popularity_less_than_expected(self, expected):
        driver = webdriver.Chrome()
        programming_languages_page = WikiNavigation(driver).go_to_programming_languages_page()

        table_data = programming_languages_page.get_table_data()

        exceptions = self._assert_popularity(table_data, expected)
        if exceptions:
            for exception in exceptions:
                print(exception)
            assert not exceptions
        
        driver.quit()

    def _assert_popularity(self, table_data: [ProgrammingLanguages], expected: int) -> [str]:
        exceptions_list = []
        for row in table_data:
            if row.popularity < expected:
                exceptions_list.append(self._build_exception_message(row, expected))
        return exceptions_list
    
    def _build_exception_message(self, row: ProgrammingLanguages, expected) -> str:
        return f"""{row.website} (Frontend:{row.frontend}|Backend:{row.backend}) has {row.popularity} unique visitors per month. (Expected more than {expected})
=========================================================================================================================================================================
                """