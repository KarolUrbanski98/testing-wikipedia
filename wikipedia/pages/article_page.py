from wikipedia.pages.wiki_page import WikiPage
from wikipedia.locators import Locators


class ArticlePage(WikiPage):

    def wait_for_title_and_compare_with_search_term(self, search_term):
        article_title = self.wait(Locators.ARTICLE_TITLE)
        assert search_term == article_title.text
        self._logger.info(f"The page title '{article_title.text}' matches search term. ->'{search_term}'")
        self._logger.info("Test completed successfully!!!")
