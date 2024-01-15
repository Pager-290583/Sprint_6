import allure
import pytest
from locators.locators import FaqLocators


class TestFaqAnswerText:
    @allure.feature('Проверка блока Вопрос-Ответ на соответствие текста в Вопросе и Ответе')
    @allure.title('Проверяем текст ответа на Вопрос')
    @allure.description('В этом тесте мы берем текст из блока Ответ и сверяем его с ожидаемым текстом ответа')
    @allure.step('Перебором сверяем текст ответа в блоке Вопрос-Ответ')
    @pytest.mark.parametrize(("text", "accordion_title", "accordion_answer"),
                             [
                                 ('Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
                                  FaqLocators.FAQ_HEAD_TITLE_0, FaqLocators.FAQ_HEAD_TEXT_0),
                                 ('Пока что у нас так: один заказ — один самокат. '
                                  'Если хотите покататься с друзьями, можете просто сделать несколько заказов '
                                  '— один за другим.', FaqLocators.FAQ_HEAD_TITLE_1, FaqLocators.FAQ_HEAD_TEXT_1),
                                 ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                                  'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                                  'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
                                  FaqLocators.FAQ_HEAD_TITLE_2, FaqLocators.FAQ_HEAD_TEXT_2),
                                 ('Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
                                  FaqLocators.FAQ_HEAD_TITLE_3, FaqLocators.FAQ_HEAD_TEXT_3),
                                 ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по '
                                  'красивому номеру 1010.', FaqLocators.FAQ_HEAD_TITLE_4, FaqLocators.FAQ_HEAD_TEXT_4),
                                 ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — '
                                  'даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
                                  FaqLocators.FAQ_HEAD_TITLE_5, FaqLocators.FAQ_HEAD_TEXT_5),
                                 ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не '
                                  'попросим. Все же свои.', FaqLocators.FAQ_HEAD_TITLE_6, FaqLocators.FAQ_HEAD_TEXT_6),
                                 ('Да, обязательно. Всем самокатов! И Москве, и Московской области.',
                                  FaqLocators.FAQ_HEAD_TITLE_7, FaqLocators.FAQ_HEAD_TEXT_7),
                             ])
    def test_faq_question_one(self, app, text, accordion_title, accordion_answer):
        app.base.open('/')
        app.base.scroll_to_bottom()
        app.base.click(accordion_title)
        assert app.base_asserts.element_text_is_correct(text, accordion_answer)