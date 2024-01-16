import random


class UserData:
    def __init__(self):
        self.name = f'Олег'
        self.family = f'Козлов'
        self.address = f'Москва, Мира 12, д. 12'
        self.station = 'Черкизовская'
        self.telephone = f'+79{random.randint(100, 999999999)}'
        self.date_zakaz = f'06.02.2024'
        self.term_data = 'сутки'
        self.comment = 'Предварительно позвонить по номеру телефона'
