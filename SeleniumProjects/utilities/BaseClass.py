import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects import home_page


@pytest.mark.usefixtures("initialise")
class BaseClass:

    def verify_text_presence(self, text):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option_from_text(self, locator, text):
        gender = Select(locator)
        gender.select_by_visible_text(text)
