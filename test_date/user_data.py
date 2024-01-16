import random
import datetime


class UserData:
    def __init__(self):
        self.name = f'Олег'
        self.family = f'Козлов'
        self.address = f'Москва, Мира 12, д. 12'
        self.station = 'Черкизовская'
        self.telephone = f'+79{random.randint(100, 999999999)}'
        self.date_zakaz = datetime.date.today().strftime("%d.%m.%Y")
        self.term_data = 'сутки'
        self.comment = 'Предварительно позвонить по номеру телефона'
