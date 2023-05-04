""" Test case
1. Open kmart website
2. Maximise the window
3. Check the url is correct
4. Close the pop up box
5. Iterate through the list of elements in the level 3 of sub menu
6. Close the window
"""

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.kmart.com.au/")
driver.maximize_window()
desiredUrl = "https://www.kmart.com.au/"
userUrl = driver.current_url
if desiredUrl == userUrl:
    print("Url verified")
else:
    print("Url is wrong")
# try:
#     driver.find_element_by_xpath("//div[@class='modal-header v2']/a//span[@class='icon-cross']").click()
# except Exception as e:
#     print(e)
# finally:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='menu-overflow']//li/a[@id='level1a_halloween']"))).click()
    time.sleep(2)
    test1 = driver.find_element_by_xpath("//ul//li[@class='level3 has-submenu']//a[@href='/category/halloween/halloween-by-category/shop-all-halloween/544501/']")
    test1.click()
    time.sleep(2)
    result1 = driver.find_elements_by_xpath("//div[@class='level4-holder open']//ul//li")
    z = len(result1)
    print(z)
    print(test1.text)
    for x in range(1, 8):
        result2 = driver.find_elements_by_xpath("//div[@class='level4-holder open']//ul//li")
        res = result2[x]
        print(res.text)
        res.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='menu-overflow']//li/a[@id='level1a_halloween']"))).click()
        time.sleep(2)
        test1 = driver.find_element_by_xpath("//ul//li[@class='level3 has-submenu']//a[@href='/category/halloween/halloween-by-category/shop-all-halloween/544501/']")
        test1.click()
        time.sleep(2)
    driver.close()


