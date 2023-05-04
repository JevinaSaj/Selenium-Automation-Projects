
from selenium.webdriver.common.by import By
from pageObjects.home_page import HomePage
from utilities.BaseClass import BaseClass


class TestMain(BaseClass):
    def test_end2end(self):
        homepage = HomePage(self.driver)
        checkout_page = homepage.shop_object()
        products = checkout_page.phone_name_objects()
        for product in products:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
        confirm_page = checkout_page.checkout_button_object()
        confirm_page.location_object().click()
        confirm_page.country_name_object().send_keys("ind")
        self.verify_text_presence("India")
        confirm_page.link_text_object().click()
        confirm_page.checkbox_object().click()
        confirm_page.purchase_button_object().click()
        success_message = confirm_page.success_message_object().text
        assert "Success! Thank you!" in success_message







