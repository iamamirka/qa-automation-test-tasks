import requests
import pytest
from bs4 import BeautifulSoup
from data.programming_languages import ProgrammingLanguages

class TestPopularity():

    url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"

    expected_cases = [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 1.5 * 10**9]

    @pytest.mark.parametrize("expected", expected_cases)
    def test_website_popularity_should_be_greater_than_expected(self, expected):
        
        table_data = self._fetch_and_parse_data_from(self.url)

        exceptions = self._assert_popularity(table_data, expected)
        if exceptions:
            for exception in exceptions:
                print(exception)
            assert not exceptions

    def _fetch_and_parse_data_from(self, url):
        response = requests.get(url)
        assert response.status_code == 200, f"Could not fetch data from {url}"

        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find('table')
        assert table is not None, "Could not find table on page"

        table_data = []
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if cells:
                raw_data = [cell.text for cell in cells]
                table_data.append(ProgrammingLanguages.map(raw_data))

        return table_data

    def _assert_popularity(self, table_data: [ProgrammingLanguages], expected: int) -> [str]:
        exceptions_list = []
        for row in table_data:
            try:
                assert row.popularity >= expected, self._build_exception_message(row, expected)
            except AssertionError as exception:
                exceptions_list.append(exception)
        
        return exceptions_list
    
    def _build_exception_message(self, row: ProgrammingLanguages, expected) -> str:
        return f"""{row.website} (Frontend:{row.frontend}|Backend:{row.backend}) has {row.popularity} unique visitors per month. (Expected more than {expected})
=========================================================================================================================================================================
                """
    
if __name__ == "__main__":
    pytest.main([__file__])