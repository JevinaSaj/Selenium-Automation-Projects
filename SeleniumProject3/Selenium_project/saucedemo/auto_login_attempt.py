""" Test case
1. direct to the website
2. maximize the window
3. get the current url
4. compare the current url with desired url and print the result
5. Enter the username
7. Then enter the password
7. If username and password is same as the defined string then click login button
8. If any of the field is wrong then clear the fields, refresh the browser and provide 3 attempts
"""



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

desiredUrl = "https://www.saucedemo.com/"
userUrl = driver.current_url
if desiredUrl == userUrl:
    print("Url verified")
else:
    print("Url is wrong")


def loginpageattempts():
    username = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]
    password = ["secret_sauce"]

    correctusername = False
    correctpassword = False
    count = 0

    while count < 3:
        username1 = input("Enter username: ")

        password1 = input("Enter password: ")


        for str1 in username:
            if str1 == username1:
                correctusername = True
                break
        if correctusername == True:
            for str2 in password:
                if str2 == password1:
                    correctpassword = True
                    break
        if correctusername == True and correctpassword == True:
            driver.find_element_by_id('user-name').send_keys("", username1)
            driver.find_element_by_name('password').send_keys("", password1)
            driver.find_element_by_xpath(("//input[@id='login-button']")).click()
            print('Access granted')
            break
        else:
            driver.find_element_by_id('user-name').send_keys("", username1)
            driver.find_element_by_name('password').send_keys("", password1)
            driver.find_element_by_xpath(("//input[@id='login-button']")).click()
            driver.refresh()
            print('Access denied. Try again.')
        count += 1



loginpageattempts()
