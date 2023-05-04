from selenium.webdriver.common.by import By

from pageObjects.confirm_page import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    phoneName = (By.XPATH, "//div[@class='card h-100']")
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def phone_name_objects(self):
        return self.driver.find_elements(*CheckoutPage.phoneName)

    def checkout_button_object(self):
        self.driver.find_element(*CheckoutPage.checkoutButton).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page







