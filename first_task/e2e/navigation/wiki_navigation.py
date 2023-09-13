from selenium import webdriver
from page_objects.programming_languages_page import ProgrammingLanguagesPage

class WikiNavigation():

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"

    def go_to_programming_languages_page(self):
        self.driver.get(self.url)
        return ProgrammingLanguagesPage(self.driver)