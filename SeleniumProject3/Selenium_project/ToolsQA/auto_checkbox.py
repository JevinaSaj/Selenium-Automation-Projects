
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class CheckBox():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def checkbox_section(self):

        self.driver.find_element_by_xpath("//div[@class='category-cards']/div[1]").click()
        self.driver.find_element_by_xpath("//div[@class='element-list collapse show']/ul[@class='menu-list']/li[@id='item-1']").click()
        self.driver.find_element_by_css_selector("span[class='rct-checkbox']").click()
        self.driver.find_element_by_css_selector("button[class='rct-option rct-option-expand-all']")

#
# obj = CheckBox()
# obj.checkbox_section()
#
