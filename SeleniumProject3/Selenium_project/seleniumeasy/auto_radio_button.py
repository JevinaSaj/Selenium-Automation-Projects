import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
desiredurl = "https://www.seleniumeasy.com/test/"
userurl = driver.current_url
if desiredurl == userurl:
    print("Url verified")
else:
    print("Url is wrong")
time.sleep(2)
driver.find_element_by_xpath("//a[@class='at-cv-button at-cv-lightbox-yesno at-cm-no-button']").click()
driver.find_element_by_id("btn_basic_example").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@class='list-group-item'][normalize-space()='Radio Buttons Demo']").click()


