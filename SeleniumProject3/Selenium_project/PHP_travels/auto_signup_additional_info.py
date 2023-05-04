
class additionalInfo():

    def additional_info(self):
        mobile_number = input("Enter your mobile number: ")
        self.driver.find_element_by_id("customfield2").send_keys("", mobile_number)
        assert self.driver.find_element_by_id("customfield2").get_attribute('value') == mobile_number

