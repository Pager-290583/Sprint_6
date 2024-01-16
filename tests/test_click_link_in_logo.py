import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.locators import LogoHeader
from test_date.constants import Constants


class TestLinkLogo:
    @allure.feature('Проверка ссылок в логотипах Самокат и Яндекс')
    @allure.title('Поверка: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    @allure.description('В этом тесте мы проверяем ссылку которая отображается в браузере '
                        'после перехода по ссылке через клик по логотипу Самокат. '
                        'Нам должна открыться страница сайта Самокат с ссылкой "https://qa-scooter.praktikum-services.ru/"')
    @allure.step('Открываем главную страницу и кликаем по логотипу Самокат')
    def test_click_logo_samokat(self, app):
        app.base.open('/')
        app.base.click(LogoHeader.LOGO_SAMOKAT)
        assert 'qa-scooter' in app.wd.current_url

    @allure.feature('Проверка ссылок в логотипах Самокат и Яндекс')
    @allure.title('Проверка: если нажать на логотип «Яндекс», попадёшь на главную страницу «Дзен».')
    @allure.description('В этом тесте мы проверяем ссылку которая отображается в браузере '
                        'после перехода по ссылке через клик по логотипу Яндекс. '
                        'Нам должна открыться главная страница сайта Дзен с ссылкой "https://dzen.ru/"')
    @allure.step('Открываем главную страницу и кликаем по логотипу Яндекс')
    def test_click_logo_yandex(self, app):
        app.base.open('/')
        app.base.click(LogoHeader.LOGO_YANDEX)
        window_after = app.wd.window_handles[1]
        app.wd.switch_to.window(window_after)
        WebDriverWait(app.wd,3).until(ec.presence_of_element_located((By.ID, 'dzen-header')))
        title = 'Дзен'
        assert title in app.wd.title



