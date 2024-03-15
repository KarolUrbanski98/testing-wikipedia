from wikipedia.pages.wiki_page import WikiPage
from wikipedia.locators import Locators


class CreateAccountPage(WikiPage):

    def enter_username(self, username):
        self._logger.info("Entering Username...")
        self.wait(Locators.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self._logger.info("Entering password...")
        self.find(Locators.PSWD_INPUT).send_keys(password)

    def enter_non_matching_password(self, password):
        self._logger.info("Entering non-matching password...")
        self.find(Locators.CONFIRM_PSWD_INPUT).send_keys(password)

    def enter_text_to_captcha(self, text):
        self._logger.info("Entering text to captcha... ")
        self.find(Locators.CAPTCHA_TEXT_INPUT).send_keys(text)

    def click_create_button(self):
        self._logger.info("Clicking create button...")
        self.find(Locators.CONFIRM_CREATE_ACCOUNT_BTN).click()

    def wait_for_error_msg_and_check_correctness(self, message):
        self._logger.info("Waiting for error message...")
        actual_error_msg = self.wait(Locators.ERROR_MSG)
        assert actual_error_msg.text == message, f"Expected text: {message}, but got: {actual_error_msg.text}"
        self._logger.info("The error message appeared and looks as expected!")
