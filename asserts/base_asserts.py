from pages.base_page import BasePage


class BaseAsserts(BasePage):

    def element_text_is_correct(self, text: str, locator: list):
        text_element = self.app.wd.find_element(*locator).text
        assert text_element == text, f"Ожидаемый текст: {text_element}. Фактический текст: {text}"
        return True