from selenium.webdriver import Keys

from wikipedia.pages.wiki_page import WikiPage
from wikipedia.locators import Locators


class WelcomePage(WikiPage):

    def input_term_into_search_box(self, search_term):
        search_box = self.wait(Locators.SEARCH_BOX)
        self._logger.info(f"typing '{search_term}'...")
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

    def click_english_version_link(self):
        self._logger.info("Going to English version...")
        return self.wait(Locators.ENGLISH_WIKIPEDIA_LINK).click()
