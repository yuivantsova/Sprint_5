import pytest
from conftest import *
from data_user import *
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructor:

    def test_mv_in_constructor_button_constructor(self, driver):

        driver.find_element(*TestLocators.BUTTON_MY_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_ON_ENTER_PAGE).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_ON_ENTER_PAGE).send_keys(password)
        driver.find_element(*TestLocators.ENTER_BUTTON_ON_PAGE_ENTER).click()

        driver.find_element(*TestLocators.BUTTON_MY_ACCOUNT).click()
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        text = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (TestLocators.HEADER_ON_MAIN_PAGE))).text

        assert text == 'Соберите бургер'



    def test_mv_in_construction_button_logo(self, driver):

        driver.find_element(*TestLocators.BUTTON_MY_ACCOUNT).click()

        driver.find_element(*TestLocators.EMAIL_INPUT_ON_ENTER_PAGE).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_ON_ENTER_PAGE).send_keys(password)
        driver.find_element(*TestLocators.ENTER_BUTTON_ON_PAGE_ENTER).click()

        driver.find_element(*TestLocators.BUTTON_MY_ACCOUNT).click()
        driver.find_element(*TestLocators.BUTTON_LOGO).click()
        text = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (TestLocators.HEADER_ON_MAIN_PAGE))).text

        assert text == 'Соберите бургер'



