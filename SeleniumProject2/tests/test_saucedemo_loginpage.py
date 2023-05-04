import pytest


@pytest.mark.usefixtures("browser_invoke")
class TestLoginPage:
    def test_login_page(self):
        self.driver.find_element_by_id('user-name').send_keys('standard_user')
        self.driver.find_element_by_name('password').send_keys('secret_sauce')
        self.driver.find_element_by_xpath(("//input[@id='login-button']")).click()