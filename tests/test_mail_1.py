import pytest


@pytest.fixture
def set_up():
    print('Пользователь зарегистрировался')

def test_sending_mail_1(set_up):
    print('Письмо отправлено')

def test_sending_mail_2(set_up):
    print('Письмо отправлено')