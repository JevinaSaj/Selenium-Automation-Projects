from auto_selenium_demo_login import toolsqa
import string
from selenium.webdriver.support.color import Color
import time

class webtable(toolsqa):
    def __init__(self):
        toolsqa.__init__(self)

    def starting(self):
        self.driver.find_element_by_xpath("//body/div[@id='app']/div[@class='body-height']/div[@class='home-content']/div[@class='home-body']/div[@class='category-cards']/div[1]").click()
        self.driver.find_element_by_xpath("//span[normalize-space()='Web Tables']").click()

    def addingElement(self):
        self.driver.find_element_by_xpath("//button[@id='addNewRecordButton']").click()
        self.driver.find_element_by_xpath("//input[@id='firstName']").click()
        # FirstName = input("Enter your first name: ")
        # driver.find_element_by_xpath("//input[@id='firstName']").send_keys("", FirstName)
        # driver.find_element_by_xpath("//input[@id='lastName']").click()
        # LastName = input("Enter your last name: ")
        # driver.find_element_by_xpath("//input[@id='lastName']").send_keys("", LastName)
        # driver.find_element_by_xpath("//input[@id='userEmail']").click()
        # Email = input("Enter your email id: ")
        # driver.find_element_by_xpath("//input[@id='userEmail']").send_keys("", Email)
        # driver.find_element_by_xpath("//input[@id='age']").click()
        # Age = input("Enter your age: ")
        # driver.find_element_by_xpath("//input[@id='age']").send_keys("", Age)
        # driver.find_element_by_xpath("//input[@id='salary']").click()
        # Salary = input("Enter your salary: ")
        # driver.find_element_by_xpath("//input[@id='salary']").send_keys("", Salary)
        # driver.find_element_by_xpath("//input[@id='department']").click()
        # Department = input("Enter your department: ")
        # driver.find_element_by_xpath("//input[@id='department']").send_keys("", Department)
        # driver.find_element_by_xpath("//button[@id='submit']").click()
        # driver.find_element_by_xpath("//input[@id='firstName']").click()
        # time.sleep(2)
        # bordercolor = driver.find_element_by_xpath("//input[@id='firstName']").value_of_css_property("border-top-color")
        # print(bordercolor)
        # time.sleep(2)
        # border = driver.find_element_by_xpath("//input[@id='firstName']").value_of_css_property("background-image")
        # print(border)
        # bordercolor = driver.find_element_by_xpath("//input[@id='firstName']").value_of_css_property("border-top-color")
        # print(bordercolor)
        # bordercolor = driver.find_element_by_xpath("//input[@id='firstName']").value_of_css_property("border-left-color")
        # print(bordercolor)
        # backgroundimage = driver.find_element_by_xpath("//input[@id='firstName']").value_of_css_property("background-image")
        # print(backgroundimage)




        






        # uppercase = list(string.ascii_uppercase)
        # lowercase = list(string.ascii_lowercase)
        # digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_', '=']










        # while True:
        #     FirstName = input("Enter your first name: ")
        #     print(len(FirstName))
        #
        #     if len(FirstName) > 0 and len(FirstName) <= 25:
        #         driver.find_element_by_xpath("//input[@id='firstName']").send_keys("", FirstName)
        #         break
        #     else:
        #         print("Name should have atleast 1 character and not more than 25 character")
        #
        # driver.find_element_by_xpath("//input[@id='lastName']").click()
        # while True:
        #     LastName = input("Enter your last name: ")
        #     print(len(LastName))
        #
        #     if len(LastName) > 0 and len(LastName) <= 25:
        #         driver.find_element_by_xpath("//input[@id='lastName']").send_keys("", LastName)
        #         break
        #     else:
        #         print("Name should have atleast 1 character and not more than 25 character")
        # #
        # driver.find_element_by_xpath("//input[@id='userEmail']").click()
        # Email = input("Enter your email id: ")
        # driver.find_element_by_xpath("//input[@id='userEmail']").send_keys("", Email)
        # driver.find_element_by_xpath("//input[@id='age']").click()
        # Age = input("Enter your age: ")
        # driver.find_element_by_xpath("//input[@id='age']").send_keys("", Age)
        # driver.find_element_by_xpath("//input[@id='salary']").click()
        # Salary = input("Enter your salary: ")
        # driver.find_element_by_xpath("//input[@id='salary']").send_keys("", Salary)
        # driver.find_element_by_xpath("//input[@id='department']").click()
        # Department = input("Enter your department: ")
        # driver.find_element_by_xpath("//input[@id='department']").send_keys("", Department)
        # driver.find_element_by_xpath("//button[@id='submit']").click()
        # driver.refresh()




obj = webtable()
obj.initialize()
obj.starting()
obj.addingElement()
