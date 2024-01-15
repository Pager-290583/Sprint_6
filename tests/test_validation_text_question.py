import allure
import pytest

from locators.locators import FaqLocators


class TestFaqQustionTitle:
    @allure.feature('Проверка блока Вопрос-Ответ на соответствие текста в Вопросе и Ответе')
    @allure.title('Проверка текста в заголовке Вопрос')
    @allure.description(
        'В этом тесте мы берем текст из заголовка Вопрос и сверяем его с ожидаемым текстом в заголовке Вопроса')
    @allure.step('Перебором сверяем заголовки блока Вопрос-Ответ')
    @pytest.mark.parametrize(("text", "locator"),
                             [
                                 ('Сколько это стоит? И как оплатить?', FaqLocators.FAQ_HEAD_TITLE_0),
                                 ('Хочу сразу несколько самокатов! Так можно?', FaqLocators.FAQ_HEAD_TITLE_1),
                                 ('Как рассчитывается время аренды?', FaqLocators.FAQ_HEAD_TITLE_2),
                                 ('Можно ли заказать самокат прямо на сегодня?', FaqLocators.FAQ_HEAD_TITLE_3),
                                 ('Можно ли продлить заказ или вернуть самокат раньше?', FaqLocators.FAQ_HEAD_TITLE_4),
                                 ('Вы привозите зарядку вместе с самокатом?', FaqLocators.FAQ_HEAD_TITLE_5),
                                 ('Можно ли отменить заказ?', FaqLocators.FAQ_HEAD_TITLE_6),
                                 ('Я жизу за МКАДом, привезёте?', FaqLocators.FAQ_HEAD_TITLE_7),
                             ])
    def test_faq_question_title(self, app, text, locator):
        app.base.open('/')
        app.base.scroll_to_bottom()
        assert app.base_asserts.element_text_is_correct(text, locator)
