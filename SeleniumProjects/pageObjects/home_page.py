from selenium.webdriver.common.by import By

from pageObjects.checkout_page import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    checkbox = (By.XPATH, "//input[@id='exampleCheck1']")
    gender = (By.CSS_SELECTOR, "[id='exampleFormControlSelect1']")
    employment = (By.XPATH, "//input[@id='inlineRadio1']")
    birthday = (By.CSS_SELECTOR, "input[name='bday']")
    submit = (By.CSS_SELECTOR, "input[class*='btn-success']")
    success = (By.CSS_SELECTOR, "div[class*='alert']")

    def shop_object(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    def name_object(self):
        return self.driver.find_element(*HomePage.name)

    def email_object(self):
        return self.driver.find_element(*HomePage.email)

    def password_object(self):
        return self.driver.find_element(*HomePage.password)

    def checkbox_object(self):
        return self.driver.find_element(*HomePage.checkbox)

    def gender_object(self):
        return self.driver.find_element(*HomePage.gender)

    def employment_object(self):
        return self.driver.find_element(*HomePage.employment)

    def birthday_object(self):
        return self.driver.find_element(*HomePage.birthday)

    def submit_object(self):
        return self.driver.find_element(*HomePage.submit)

    def success_object(self):
        return self.driver.find_element(*HomePage.success)

