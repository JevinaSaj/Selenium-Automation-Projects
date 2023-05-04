import pytest

from pageObjects.home_page import HomePage
from testData.homepageData import home_page_data
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_details_submission_page(self, get_data):
        home_page = HomePage(self.driver)
        home_page.name_object().send_keys(get_data["Name"])
        home_page.email_object().send_keys(get_data["Email"])
        home_page.password_object().send_keys(get_data["Password"])
        home_page.checkbox_object().click()
        self.select_option_from_text(home_page.gender_object(), get_data["Gender"])
        home_page.employment_object().click()
        home_page.birthday_object().send_keys(get_data["Birthday"])
        home_page.submit_object().click()
        success_message = home_page.success_object().text
        assert "Success!" in success_message
        self.driver.refresh()

    @pytest.fixture(params=home_page_data.data_homepage)
    def get_data(self, request):
        return request.param


