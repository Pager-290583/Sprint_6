from selenium.webdriver.common.by import By


class OrderLocators:
    NAME_INPUT = By.CSS_SELECTOR, '[class*="Order_Form"] [placeholder="* Имя"]'
    FAMILY_INPUT = By.CSS_SELECTOR, '[class*="Order_Form"] [placeholder="* Фамилия"]'
    ADDRESS_INPUT = By.CSS_SELECTOR, '[class*="Order_Form"] [placeholder="* Адрес: куда привезти заказ"]'
    STATION_LIST = By.CSS_SELECTOR, '[class*="Order_Form"] [placeholder="* Станция метро"]'
    TELEPHONE_INPUT = By.CSS_SELECTOR, '[class*="Order_Form"] [placeholder="* Телефон: на него позвонит курьер"]'
    DATE_INPUT = By.CSS_SELECTOR, '[class*="Order_Form"] [placeholder="* Когда привезти самокат"]'
    CHOOSE_DATA = By.XPATH, '//div[@class="react-datepicker__day react-datepicker__day--001"]'
    TERM_DATA = By.XPATH, "//div[@class='Dropdown-control']"
    COLOR_BLACK_CHECKBOX = By.XPATH, "//input[@id='black']"
    COLOR_GREY_CHECKBOX = By.XPATH, "//input[@id='gray']"
    COMMENT_INPUT = By.CSS_SELECTOR, '[class*="Order_Form"] [placeholder="Комментарий для курьера"]'
    BUTTON = By.CSS_SELECTOR, '[class*="Order_NextButton"] [class*="Button_Button"]'
    THREE_BUTTON = By.CSS_SELECTOR, "[class*='Home_ThirdPart'] [class*='Button_Button']"
    BUTTON_ZAKAZ = By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/button[2]'
    BUTTON_ZAKAZ_PASS = By.CSS_SELECTOR, 'div.App_App__15LM- div.Order_Content__bmtHS div.Order_Modal__YZ-d3 div.Order_Buttons__1xGrp > button.Button_Button__ra12g.Button_Middle__1CSJM:nth-child(2)'


class FaqLocators:
    FAQ_SECTION = By.CSS_SELECTOR, '[class*="Home_FAQ"]'
    FAQ_HEAD_TITLE_0 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-0"]'
    FAQ_HEAD_TEXT_0 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-0"]'
    FAQ_HEAD_TITLE_1 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-1"]'
    FAQ_HEAD_TEXT_1 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-1"]'
    FAQ_HEAD_TITLE_2 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-2"]'
    FAQ_HEAD_TEXT_2 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-2"]'
    FAQ_HEAD_TITLE_3 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-3"]'
    FAQ_HEAD_TEXT_3 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-3"]'
    FAQ_HEAD_TITLE_4 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-4"]'
    FAQ_HEAD_TEXT_4 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-4"]'
    FAQ_HEAD_TITLE_5 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-5"]'
    FAQ_HEAD_TEXT_5 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-5"]'
    FAQ_HEAD_TITLE_6 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-6"]'
    FAQ_HEAD_TEXT_6 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-6"]'
    FAQ_HEAD_TITLE_7 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-7"]'
    FAQ_HEAD_TEXT_7 = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-7"]'


class TextOrderPass:
    TEXT_ORDER_PASS = By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]'


class LogoHeader:
    LOGO_SAMOKAT = By.CSS_SELECTOR, '[class*="Header_Logo"] [alt="Scooter"]'
    LOGO_YANDEX = By.CSS_SELECTOR, '[class*="Header_Logo"] [alt="Yandex"]'