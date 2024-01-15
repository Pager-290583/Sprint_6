import allure
import pytest


from application import Application
from test_date.constants import Constants
from test_date.user_data import UserData


@allure.title('Браузер')
@pytest.fixture(scope="function")
def app(request):
    with allure.step('Запуск браузера'):
        app = Application(base_url=Constants.URL)
    yield app
    with allure.step('Закрытие браузера'):
        app.destroy()


@pytest.fixture()
def user_data():
    user_data = UserData()
    return user_data
