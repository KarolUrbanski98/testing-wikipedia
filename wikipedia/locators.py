from selenium.webdriver.common.by import By


class Locators:
    SEARCH_BOX = (By.NAME, "search")
    ARTICLE_TITLE = (By.CSS_SELECTOR, ".mw-page-title-main")
    ENGLISH_WIKIPEDIA_LINK = (By.ID, "js-link-box-en")
    CREATE_ACCOUNT_BTN = (By.ID, "pt-createaccount-2")
    USERNAME_INPUT = (By.ID, "wpName2")
    PSWD_INPUT = (By.ID, "wpPassword2")
    CONFIRM_PSWD_INPUT = (By.ID, "wpRetype")
    CAPTCHA_TEXT_INPUT = (By.ID, "mw-input-captchaWord")
    CONFIRM_CREATE_ACCOUNT_BTN = (By.ID, "wpCreateaccount")
    ERROR_MSG = (By.CLASS_NAME, "mw-message-box:nth-child(2)")
