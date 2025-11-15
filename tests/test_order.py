# Импортируем библиотеку pytest для написания и запуска тестов
import pytest


# Декоратор @pytest.mark.run(order=2) указывает, что этот тест должен выполняться вторым по счёту
@pytest.mark.run(order=2)
def test_method_1(set_up):
    print('Метод 1')


# Декоратор @pytest.mark.run(order=3) указывает, что этот тест должен выполняться третьим по счёту
@pytest.mark.run(order=3)
def test_method_2(set_up):
    print('Метод 2')


# Декоратор @pytest.mark.run(order=1) указывает, что этот тест должен выполняться первым по счёту
@pytest.mark.run(order=1)
def test_method_3(set_up):
    print('Метод 3')


# Декоратор @pytest.mark.run(order=6) указывает, что этот тест должен выполняться шестым по счёту
@pytest.mark.run(order=6)
def test_method_4(set_up):
    print('Метод 4')


# Декоратор @pytest.mark.run(order=4) указывает, что этот тест должен выполняться четвёртым по счёту
@pytest.mark.run(order=4)
def test_method_5(set_up):
    print('Метод 5')


# Декоратор @pytest.mark.run(order=5) указывает, что этот тест должен выполняться пятым по счёту
@pytest.mark.run(order=5)
def test_method_6(set_up):
    print('Метод 6')