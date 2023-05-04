import string


class passwordSection():

    def password(self):
        password = list(input("Enter password: "))
        self.driver.find_element_by_id("inputNewPassword1").send_keys("", password)
        LENGTH = 8
        uppercase = list(string.ascii_uppercase)
        lowercase = list(string.ascii_lowercase)
        digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_', '=']
        upcase = False
        lowcase = False
        digi = False
        spec = False
        if any(x in uppercase for x in password):
            upcase = True
            print("Uppercase found")
        if any(x in lowercase for x in password):
            lowcase = True
            print("lowercase found")
        if any(x in digit for x in password):
            digi = True
            print("digit found")
        if any(x in special for x in password):
            spec = True
            print("Special character found")

        length = len(password)
        strong = upcase and lowcase and digi and spec and length > LENGTH

        if not strong:
            print(self.driver.find_element_by_css_selector("div[class='password-strength-meter'] p").text)

        else:
            print(self.driver.find_element_by_css_selector("div[class='password-strength-meter'] p").text)

        while True:

            confirm_password = list(input("confirm password: "))
            self.driver.find_element_by_id("inputNewPassword2").send_keys("", confirm_password)

            if password == confirm_password:
                print("Password is confirmed")
                break
            else:
                print("Re entered password is wrong")

