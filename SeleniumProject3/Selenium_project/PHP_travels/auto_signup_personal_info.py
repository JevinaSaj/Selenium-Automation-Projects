from selenium.webdriver.common.by import By
import re


class personalInfoSection():

    def personal_info(self):
        firstName = input("Enter your first name: ")
        self.driver.find_element(By.ID, "inputFirstName").send_keys("", firstName)
        lastName = input("Enter your last name: ")
        self.driver.find_element(By.ID, "inputLastName").send_keys("", lastName)

        while True:
            email = input("Enter your email: ")
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if re.search(regex, email):
                print("Valid Email")
                break
            else:
                print("Invalid Email, please include '@' and '.' extensions in th email address")

        self.driver.find_element(By.ID, "inputEmail").send_keys("", email)
        self.driver.find_element(By.XPATH, "//div[@class='selected-dial-code']").click()
        result = self.driver.find_elements(By.XPATH, "//ul[@class='country-list']//li")
        x = len(result)
        print(x)
        for res in result:
            x = 0
            if x < 247:
                res.click()
                self.driver.find_element(By.XPATH, "//div[@class='selected-dial-code']").click()
                print(res.text)
        phone_number = input("Enter your phone number without country code: ")
        self.driver.find_element(By.ID, "inputPhone").click()
        self.driver.find_element(By.ID, "inputPhone").send_keys("", phone_number)

