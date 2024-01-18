import allure
from locators.locators import TextOrderPass
from test_date.constants import Constants


class TestButtonFooter:
    @allure.feature("Проверка формы заказа")
    @allure.title('Тестирование формы заказа через кнопку Заказать в подвале сайта')
    @allure.description('В этом тесте мы проверяем оформление заказа через кнопку заказа в Хедере сайта.'
                        'Тест кликает по кнопке в шапке. Заполняет все поля и сверяется по тексту Заказ оформлен')
    @allure.step('Заполненяем поля формы заказа')
    def test_button_footer(self, app, user_data):
        app.base.open('/')
        app.zakaz_main_page.scroll_zakaz(user_data.name,
                                         user_data.family,
                                         user_data.address,
                                         user_data.station,
                                         user_data.telephone,
                                         user_data.date_zakaz,
                                         user_data.term_data,
                                         user_data.comment
                                         )
        text_element = app.wd.find_element(*TextOrderPass.TEXT_ORDER_PASS).text
        assert Constants.text_order in text_element, f'Ожидаемый текст: {Constants.text_order}. Фактический текст: {text_element}'
