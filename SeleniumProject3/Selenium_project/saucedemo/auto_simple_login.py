"""Test case
1. direct to the website
2. maximize the window
3. get the current url
4. compare the current url with desired url and print the result
5. enter username and password using send_keys
6. click the login buttons
7. close the window"""


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class login():
    def username_password(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        desiredUrl = "https://www.saucedemo.com/"
        userUrl = driver.current_url
        if desiredUrl == userUrl:
            print("Url verified")
        else:
            print("Url is wrong")
        driver.find_element_by_id('user-name').send_keys('standard_user')
        driver.find_element_by_name('password').send_keys('secret_sauce')
        driver.find_element_by_xpath(("//input[@id='login-button']")).click()
        time.sleep(4)
        driver.close()



findbyid = login()
findbyid.username_password()

