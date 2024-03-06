import pytest
from conftest import *
from data_user import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestPersonalAccount:

    def test_move_personal_account(self, driver):

        driver.find_element(*TestLocators.BUTTON_MY_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_ON_ENTER_PAGE).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_ON_ENTER_PAGE).send_keys(password)
        driver.find_element(*TestLocators.ENTER_BUTTON_ON_PAGE_ENTER).click()
        driver.find_element(*TestLocators.BUTTON_MY_ACCOUNT).click()
        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.PAGE_MY_ACCOUNT)).text
        assert text == 'Профиль'
