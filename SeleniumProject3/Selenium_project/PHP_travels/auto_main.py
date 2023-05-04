"""Test case
1. direct to the website
2. maximize the window
3. get the current url
4. compare the current url with desired url and print the result
5. Enter personal details
6. display every phone code
7. enter the billing address
8. display every country names in the billing address
9. enter mobile number
10. verify if the entered password id strong
11. confirm the password
12. click the recaptcha
13. click register
14. display the error messages if any present"""

from auto_signup_additional_info import additionalInfo
from auto_signup_billing_address import billingAddress
from auto_signup_password import passwordSection
from auto_signup_personal_info import personalInfoSection
from auto_signup_recaptcha import recaptchaSection
from auto_signup import SetDriver


class mainSection(SetDriver, personalInfoSection, billingAddress, additionalInfo, passwordSection, recaptchaSection):

    def alert(self):
        alert = self.driver.find_elements_by_css_selector("div[class='alert alert-danger'] ul li")
        print("The following errors occured : ")
        for opt in alert:
            print(opt.text)


obj = mainSection()
obj.initialise()
obj.personal_info()
obj.billing_address()
obj.additional_info()
obj.password()
obj.recaptcha()
obj.alert()

