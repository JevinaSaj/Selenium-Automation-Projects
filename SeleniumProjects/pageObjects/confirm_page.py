from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    location = (By.CSS_SELECTOR, "button[class*='btn-success']")
    countryName = (By.ID, "country")
    linkText = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR, "input[class*='btn-success']")
    successMessage = (By.CLASS_NAME, "alert-success")

    def location_object(self):
        return self.driver.find_element(*ConfirmPage.location)

    def country_name_object(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def link_text_object(self):
        return self.driver.find_element(*ConfirmPage.linkText)

    def checkbox_object(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def purchase_button_object(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def success_message_object(self):
        return self.driver.find_element(*ConfirmPage.successMessage)



