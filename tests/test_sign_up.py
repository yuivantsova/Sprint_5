import pytest
from conftest import *
from data_user import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestSignUp:

    def test_sign_up_button_enter(self, driver):
        driver.find_element(*TestLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_ON_ENTER_PAGE).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_ON_ENTER_PAGE).send_keys(password)
        driver.find_element(*TestLocators.ENTER_BUTTON_ON_PAGE_ENTER).click()

        text = WebDriverWait(driver, 3).until(
             (expected_conditions.visibility_of_element_located(TestLocators.HEADER_ON_MAIN_PAGE))).text

        assert text == 'Соберите бургер'

    def test_sign_up_button_my_account(self, driver):
        driver.find_element(*TestLocators.BUTTON_MY_ACCOUNT).click()

        driver.find_element(*TestLocators.EMAIL_INPUT_ON_ENTER_PAGE).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_ON_ENTER_PAGE).send_keys(password)
        driver.find_element(*TestLocators.ENTER_BUTTON_ON_PAGE_ENTER).click()
        text = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.HEADER_ON_MAIN_PAGE))).text

        assert text == 'Соберите бургер'

    def test_sign_up_button_reg(self, driver):
        driver.find_element(*TestLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.REGISTER_BUTTON_ON_ENTER_PAGE).click()
        driver.find_element(*TestLocators.BUTTON_ENTER_ON_REG_PAGE).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_ON_ENTER_PAGE).send_keys(email)

        driver.find_element(*TestLocators.PASSWORD_INPUT_ON_ENTER_PAGE).send_keys(password)
        driver.find_element(*TestLocators.ENTER_BUTTON_ON_PAGE_ENTER).click()
        text = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.HEADER_ON_MAIN_PAGE))).text

        assert text == 'Соберите бургер'


    def test_sign_up_button_pass_recovery(self, driver):
        driver.find_element(*TestLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.BUTTON_RECOVERY_PASS).click()
        driver.find_element(*TestLocators.BUTTON_ENTER_ON_RECOVERY_PAGE).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_ON_ENTER_PAGE).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_ON_ENTER_PAGE).send_keys(password)
        driver.find_element(*TestLocators.ENTER_BUTTON_ON_PAGE_ENTER).click()
        text = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.HEADER_ON_MAIN_PAGE))).text

        assert text == 'Соберите бургер'

