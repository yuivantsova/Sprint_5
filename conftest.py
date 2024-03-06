import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    url = "https://stellarburgers.nomoreparties.site"
    driver.get(url)
    yield driver
    driver.quit()
