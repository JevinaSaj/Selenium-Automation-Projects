import re
import string
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://phptravels.org/register.php")
desiredUrl = "https://phptravels.org/register.php"
driver.maximize_window()
userUrl = driver.current_url
if desiredUrl == userUrl:
    print("Url verified")
else:
    print("Url is wrong")

firstName = input("Enter your first name: ")
driver.find_element(By.ID, "inputFirstName").send_keys("", firstName)
lastName = input("Enter your last name: ")
driver.find_element(By.ID, "inputLastName").send_keys("", lastName)
while True:
    email = input("Enter your email: ")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.search(regex, email):
        print("Valid Email")
        break
    else:
        print("Invalid Email, please include '@' in th email address")

driver.find_element(By.ID, "inputEmail").send_keys("", email)
driver.find_element(By.XPATH, "//div[@class='selected-dial-code']").click()
phone_number = input("Enter your phone number without country code: ")
driver.find_element(By.ID, "inputPhone").click()
driver.find_element(By.ID, "inputPhone").send_keys("", phone_number)
company_name = input("Enter your company name(optional) : ")
driver.find_element(By.ID, "inputCompanyName").send_keys("", company_name)
street_address1 = input("Enter your street address1: ")
driver.find_element(By.ID, "inputAddress1").send_keys("", street_address1)
street_address2 = input("Enter your street address2: ")
driver.find_element(By.ID, "inputAddress2").send_keys("", street_address2)
city = input("Enter your city name: ")
driver.find_element(By.ID, "inputCity").send_keys("", city)
state = input("Enter your state name: ")
driver.find_element(By.ID, "stateinput").send_keys("", state)
postcode = input("Enter your postcode name: ")
driver.find_element(By.ID, "inputPostcode").send_keys("", postcode)
dropdown = Select(driver.find_element_by_xpath("//select[@id='inputCountry']"))
dropdown.select_by_visible_text("India")
mobile_number = input("Enter your mobile number: ")
driver.find_element_by_id("customfield2").send_keys("", mobile_number)
password = list(input("Enter password: "))
driver.find_element_by_id("inputNewPassword1").send_keys("", password)
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
    print(driver.find_element_by_css_selector("div[class='password-strength-meter'] p").text)

else:
    print(driver.find_element_by_css_selector("div[class='password-strength-meter'] p").text)

while True:

    confirm_password = list(input("confirm password: "))
    driver.find_element_by_id("inputNewPassword2").send_keys("", confirm_password)

    if password == confirm_password:
        print("Password is confirmed")
        break
    else:
        print("Re entered password is wrong")
        driver.find_element_by_id("inputNewPassword2").clear()

mainWin = driver.current_window_handle
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
time.sleep(30)
driver.switch_to.window(mainWin)
time.sleep(20)
driver.find_element_by_xpath("//input[@value='Register']").click()






