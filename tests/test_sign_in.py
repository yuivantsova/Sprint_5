import random
import pytest
from conftest import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from function import *


class TestSignIn:


    @pytest.mark.parametrize('name, email, password', [
        ['Юлиана', f'{RandomDataUser.random_email(5)}', f'{RandomDataUser.random_password(6)}'],
        ['Мария-Елена', f'{RandomDataUser.random_email(4)}', f'{RandomDataUser.random_password(7)}'],
        ['Anna', f'{RandomDataUser.random_email(6)}', f'{RandomDataUser.random_password(10)}']
    ])
    def test_sign_in_data_true(self, driver, name, email, password):

        driver.find_element(*TestLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.REGISTER_BUTTON_ON_ENTER_PAGE).click()

        driver.find_element(*TestLocators.NAME_INPUT_ON_REG_PAGE).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_INPUT_ON_REG_PAGE).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_ON_REG_PAGE).send_keys(password)
        driver.find_element(*TestLocators.REGISTER_BUTTON_ON_REG_PAGE).click()
        text = WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_ON_ENTER_PAGE)).text

        assert text == 'Вход'

    @pytest.mark.parametrize('name, email, password', [['Ю', f'yuivantsova6{random.randint(100, 999)}@gmail.com', f'{RandomDataUser.random_password(5)}'],
                                                       ['Мария-Елена', f'yuivantsova6{random.randint(100, 999)}@gmail.com', f'{RandomDataUser.random_password(3)}']
                             ])
    def test_sign_in_password_false(self, driver, name, email, password):

        driver.find_element(*TestLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.REGISTER_BUTTON_ON_ENTER_PAGE).click()

        driver.find_element(*TestLocators.NAME_INPUT_ON_REG_PAGE).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_INPUT_ON_REG_PAGE).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_ON_REG_PAGE).send_keys(password)
        driver.find_element(*TestLocators.REGISTER_BUTTON_ON_REG_PAGE).click()
        text = WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_INVALID_PASSWORD_ON_REG_PAGE)).text

        assert text == 'Некорректный пароль'


    @pytest.mark.parametrize('name, email, password',
                             [['', f'yuivantsova6{random.randint(100, 999)}@gmail.com', f'{RandomDataUser.random_password(6)}']])
    def test_sign_in_empty_name(self, driver, name, email, password):

        driver.find_element(*TestLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.REGISTER_BUTTON_ON_ENTER_PAGE).click()

        driver.find_element(*TestLocators.NAME_INPUT_ON_REG_PAGE).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_INPUT_ON_REG_PAGE).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_ON_REG_PAGE).send_keys(password)
        driver.find_element(*TestLocators.REGISTER_BUTTON_ON_REG_PAGE).click()

        text = driver.find_element(*TestLocators.HEADER_ON_REG_PAGE).text

        assert text == 'Регистрация'
