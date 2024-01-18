import allure
from selenium import webdriver

from asserts.base_asserts import BaseAsserts
from pages.base_page import BasePage
from pages.zakaz_page_main import ZakazMainPage
from pages.zakaz_page_order import ZakazPageSamokat


class Application:

    def __init__(self, base_url):
        self.base_url = base_url
        self.base = BasePage(self)
        self.zakaz_page = ZakazPageSamokat(self)
        self.zakaz_main_page = ZakazMainPage(self)
        self.base_asserts = BaseAsserts(self)
        self.wd = webdriver.Firefox()

    @allure.step('Завершение сессии')
    def destroy(self):
        self.wd.quit()