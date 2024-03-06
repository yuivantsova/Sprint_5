import pytest
from conftest import *
from data_user import *
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestSwitchConstructor:

    def test_switch_constructor_sauces(self, driver):

        driver.find_element(*TestLocators.BUTTON_MY_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_ON_ENTER_PAGE).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_ON_ENTER_PAGE).send_keys(password)
        driver.find_element(*TestLocators.ENTER_BUTTON_ON_PAGE_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TAB_SAUCES))
        driver.find_element(*TestLocators.TAB_SAUCES).click()
        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_TAB_SAUCES)).text
        assert text == "Соусы"

    def test_switch_constructor_topping(self, driver):

        driver.find_element(*TestLocators.BUTTON_MY_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_ON_ENTER_PAGE).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_ON_ENTER_PAGE).send_keys(password)
        driver.find_element(*TestLocators.ENTER_BUTTON_ON_PAGE_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TAB_TOPPING))
        driver.find_element(*TestLocators.TAB_TOPPING).click()
        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_TAB_TOPPING)).text
        assert text == "Начинки"

    def test_switch_constructor_buns(self, driver):

        driver.find_element(*TestLocators.BUTTON_MY_ACCOUNT).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_ON_ENTER_PAGE).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_ON_ENTER_PAGE).send_keys(password)
        driver.find_element(*TestLocators.ENTER_BUTTON_ON_PAGE_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TAB_SAUCES))
        driver.find_element(*TestLocators.TAB_SAUCES).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_TAB_SAUCES))
        driver.find_element(*TestLocators.TAB_BUNS).click()
        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_TAB_BUNS)).text
        assert text == "Булки"
