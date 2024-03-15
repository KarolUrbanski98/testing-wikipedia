from wikipedia.pages.welcome_page import WelcomePage
from wikipedia.pages.article_page import ArticlePage
from wikipedia.pages.main_page import MainPage
from wikipedia.pages.create_account_page import CreateAccountPage


def test_wikipedia_search(driver, search_terms):
    welcome_page = WelcomePage(driver)
    welcome_page.input_term_into_search_box(search_terms)
    article_page = ArticlePage(driver)
    article_page.wait_for_title_and_compare_with_search_term(search_terms)


def test_password_matching_verification(driver):
    welcome_page = WelcomePage(driver)
    welcome_page.click_english_version_link()
    main_page = MainPage(driver)
    main_page.click_create_account_button()
    create_account_page = CreateAccountPage(driver)
    create_account_page.enter_username("Seleniummm testing")
    create_account_page.enter_password("Pass1234!")
    create_account_page.enter_non_matching_password("password123")
    create_account_page.enter_text_to_captcha("qwerty")
    create_account_page.click_create_button()
    create_account_page.wait_for_error_msg_and_check_correctness("The passwords you entered do not match.")
