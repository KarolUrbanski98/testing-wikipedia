import pytest
import json
import random
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = get_driver("firefox")
    driver.get("https://www.wikipedia.org/")
    driver.maximize_window()
    yield driver
    driver.quit()


def get_driver(browser):
    if browser == "firefox":
        return webdriver.Firefox()
    elif browser == "chrome":
        return webdriver.Chrome()
    else:
        raise ValueError(f"Not supported browser: {browser}")


def pytest_generate_tests(metafunc):
    if "search_terms" in metafunc.fixturenames:
        terms = choose_search_terms()
        metafunc.parametrize("search_terms", terms)


def import_search_terms():
    with open("terms.json", "r") as file:
        data = json.load(file)
        return data["searchTerms"]


def choose_search_terms(amount=6):
    terms = import_search_terms()
    terms_amount = min(amount, len(terms))
    selected_terms = random.sample(terms, terms_amount)
    return selected_terms
