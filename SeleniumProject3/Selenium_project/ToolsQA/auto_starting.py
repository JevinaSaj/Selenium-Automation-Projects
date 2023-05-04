
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Staring():
    def __init__(self):

        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def initialize(self, a):
        self.driver.get(a)
        self.driver.maximize_window()
        desiredurl = a
        userurl = self.driver.current_url
        if desiredurl == userurl:
            print("Url verified")
        else:
            print("Url is wrong")

obj = Staring()
obj.initialize("https://demoqa.com/")
obj.checkbox_section()
