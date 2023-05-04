
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class SetDriver:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def initialise(self):
        self.driver.get("https://phptravels.org/register.php")
        desiredUrl = "https://phptravels.org/register.php"
        self.driver.maximize_window()
        userUrl = self.driver.current_url
        if desiredUrl == userUrl:
            print("Url verified")
        else:
            print("Url is wrong")

        self.driver.find_element_by_xpath("//ul[@class='top-nav']//a[normalize-space()='Register']").click()






