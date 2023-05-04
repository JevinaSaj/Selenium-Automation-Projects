from selenium.webdriver.support.select import Select

class billingAddress():

    def billing_address(self):
        company_name = input("Enter your company name(optional) : ")
        self.driver.find_element_by_id("inputCompanyName").send_keys("", company_name)
        assert self.driver.find_element_by_id("inputCompanyName").get_attribute('value') == company_name

        street_address1 = input("Enter your street address1: ")
        self.driver.find_element_by_id("inputAddress1").send_keys("", street_address1)
        assert self.driver.find_element_by_id("inputAddress1").get_attribute('value') == street_address1

        street_address2 = input("Enter your street address2: ")
        self.driver.find_element_by_id("inputAddress2").send_keys("", street_address2)
        assert self.driver.find_element_by_id("inputAddress2").get_attribute('value') == street_address2

        city = input("Enter your city name: ")
        self.driver.find_element_by_id("inputCity").send_keys("", city)
        assert  self.driver.find_element_by_id("inputCity").get_attribute('value') == city

        state = input("Enter your state name: ")
        self.driver.find_element_by_id("stateinput").send_keys("", state)
        assert self.driver.find_element_by_id("stateinput").get_attribute('value') == state

        postcode = input("Enter your postcode name: ")
        self.driver.find_element_by_id("inputPostcode").send_keys("", postcode)
        assert self.driver.find_element_by_id("inputPostcode").get_attribute('value') == postcode

        dropdown = Select(self.driver.find_element_by_xpath("//select[@id='inputCountry']"))
        y = dropdown.options
        z = len(y)
        print(z)

        for opt in y:
            z = 0
            if z < 248:
                print(opt.text)
                opt.click()


