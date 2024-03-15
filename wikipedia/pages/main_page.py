from wikipedia.pages.wiki_page import WikiPage
from wikipedia.locators import Locators


class MainPage(WikiPage):

    def click_create_account_button(self):
        self._logger.info("Clicking 'Create account' button...")
        return self.wait(Locators.CREATE_ACCOUNT_BTN).click()
