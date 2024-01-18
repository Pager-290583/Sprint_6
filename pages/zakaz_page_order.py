import allure
from selenium.webdriver import Keys

from locators.locators import OrderLocators
from pages.base_page import BasePage


class ZakazPageSamokat(BasePage):
    @allure.step('Заполнение полей вылидными данными и нажание на кнопку Заказать')
    def zakaz(self, name, family, address, station, telephone, date_zakaz, term_data, comment):
        self.enter_text(name, OrderLocators.NAME_INPUT)
        self.enter_text(family, OrderLocators.FAMILY_INPUT)
        self.enter_text(address, OrderLocators.ADDRESS_INPUT)
        self.choose_value_in_select(station, OrderLocators.STATION_LIST)
        self.enter_text(telephone, OrderLocators.TELEPHONE_INPUT)
        self.click(OrderLocators.BUTTON)
        self.enter_text(date_zakaz, OrderLocators.DATE_INPUT)
        self.enter_text(Keys.ENTER, OrderLocators.DATE_INPUT)
        self.choose_value_in_select(term_data, OrderLocators.TERM_DATA)
        self.click(OrderLocators.COLOR_BLACK_CHECKBOX)
        self.enter_text(comment, OrderLocators.COMMENT_INPUT)
        self.click(OrderLocators.BUTTON_ZAKAZ)
        self.click(OrderLocators.BUTTON_ZAKAZ_PASS)