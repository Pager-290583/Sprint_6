import allure
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.locators import FaqLocators


class BasePage:

    def __init__(self, app):
        self.app = app

    @allure.step('Открытие страницы')
    def open(self, url: str):
        self.app.wd.get(f"{self.app.base_url}{url}")

    @allure.step('Ввод текста')
    def enter_text(self, text: str, locator: list):
        self.app.wd.find_element(*locator).send_keys(text)

    @allure.step('Ввод текста в поле всплывающего списка с поиском')
    def enter_text_select_input(self, text: str, locator: list):
        self.click(locator)
        self.enter_text(text, locator)
        self.enter_text(Keys.TAB, locator)

    @allure.step('Выбор значения из выпадающего списка по тексту элемента')
    def choose_value_in_select(self, select_value: str, select_locator: list):
        self.click(select_locator)
        self.click([By.XPATH, f"//*[text()='{select_value}']"])

    @allure.step('Кликаем по кнопке')
    def click(self, locator):
        self.app.wd.find_element(*locator).click()

    @allure.step('Наведение курсора на элемент')
    def hover(self, locator):
        element = self.app.wd.find_element(*locator)
        ActionChains(self.app.wd).move_to_element(element).perform()

    @allure.step('Скролл к концу страницы')
    def scroll_to_bottom(self):
        self.app.wd.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        WebDriverWait(self.app.wd, 3).until(ec.visibility_of_element_located(FaqLocators.FAQ_SECTION))
