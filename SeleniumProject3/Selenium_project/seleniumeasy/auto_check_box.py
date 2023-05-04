"""Test case
1. Open the website
2. Maximize the window
3. verify the url with desired url
4. Click the 'no thanks' button in the popup box
5. Click 'start practising'
6. Click 'check box demo'
7. Click on single check box demo
8. Verify the display message and its style
9. Check the status of the 'click all' button in the multiple check box demo
10. Click on 'check all' button in the multiple check box demo
11. Check the status of the 'click all' button turn to 'uncheck all'
12. Uncheck at least 2 check boxes and the button turns back to 'check all'
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class auto_check_box():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def starting(self):
        self.driver.get("https://www.seleniumeasy.com/test/")
        self.driver.maximize_window()
        desiredurl = "https://www.seleniumeasy.com/test/"
        userurl = self.driver.current_url
        if desiredurl == userurl:
            print("Url verified")
        else:
            print("Url is wrong")
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@class='at-cv-button at-cv-lightbox-yesno at-cm-no-button']").click()
        self.driver.find_element_by_id("btn_basic_example").click()
        time.sleep(2)

    def checkBoxSingle(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Check Box Demo']").click()
        time.sleep(2)
        self.driver.find_element_by_id("isAgeSelected").click()
        availabletext = self.driver.find_element_by_id("txtAge").text
        print(availabletext)
        desiredtext = "Success - Check box is checked"
        if availabletext == desiredtext:
            print("Text verified")
        else:
            print("Text is wrong")

        fontsize = self.driver.find_element_by_id("txtAge").value_of_css_property("font-size")
        print("Font size :", fontsize)
        color = self.driver.find_element_by_id("txtAge").value_of_css_property("color")
        print("Font color :", color)
        textalign = self.driver.find_element_by_id("txtAge").value_of_css_property("text-align")
        print("Text aligin :", textalign)
        fontfamily = self.driver.find_element_by_id("txtAge").value_of_css_property("font-family")
        print("Font family :", fontfamily)
        lineheight = self.driver.find_element_by_id("txtAge").value_of_css_property("line-height")
        print("Line height :", lineheight)

    def checkBoxMultiple(self):
        time.sleep(2)
        checkall = self.driver.find_element_by_id("check1").get_attribute("value")
        print("Status :", checkall)
        if checkall == "Check All":
            self.driver.find_element_by_id("check1").click()
        uncheckall = self.driver.find_element_by_id("check1").get_attribute("value")
        print("Status :", uncheckall)
        if uncheckall == "Uncheck All":
            time.sleep(2)
            self.driver.find_element_by_xpath("//label[normalize-space()='Option 1']").click()
            x = self.driver.find_element_by_id("check1").get_attribute("value")
            print("Status :", x)
            time.sleep(2)
            self.driver.find_element_by_xpath("//label[normalize-space()='Option 2']").click()
            y = self.driver.find_element_by_id("check1").get_attribute("value")
            print("Status :", y)
            time.sleep(2)
            self.driver.find_element_by_id("check1").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//label[normalize-space()='Option 2']").click()
            x = self.driver.find_element_by_id("check1").get_attribute("value")
            print("Status :", x)
            time.sleep(2)
            self.driver.find_element_by_xpath("//label[normalize-space()='Option 3']").click()
            y = self.driver.find_element_by_id("check1").get_attribute("value")
            print("Status :", y)
            time.sleep(2)
            self.driver.find_element_by_id("check1").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//label[normalize-space()='Option 3']").click()
            x = self.driver.find_element_by_id("check1").get_attribute("value")
            print("Status :", x)
            time.sleep(2)
            self.driver.find_element_by_xpath("//label[normalize-space()='Option 4']").click()
            y = self.driver.find_element_by_id("check1").get_attribute("value")
            print("Status :", y)
            self.driver.close()

# obj = auto_check_box()
# obj.starting()
# obj.checkBoxSingle()
# obj.checkBoxMultiple()













