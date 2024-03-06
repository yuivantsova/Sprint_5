import pytest
from conftest import *
from data_user import *
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestExit:

    def test_exit_personal_account(self, driver):

        driver.find_element(*TestLocators.BUTTON_MY_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_ON_ENTER_PAGE).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_ON_ENTER_PAGE).send_keys(password)
        driver.find_element(*TestLocators.ENTER_BUTTON_ON_PAGE_ENTER).click()
        driver.find_element(*TestLocators.BUTTON_MY_ACCOUNT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGOUT))
        driver.find_element(*TestLocators.BUTTON_LOGOUT).click()
        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_ON_ENTER_PAGE)).text
        assert text == 'Вход'