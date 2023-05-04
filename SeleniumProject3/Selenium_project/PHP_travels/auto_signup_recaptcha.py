
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class recaptchaSection():

    def recaptcha(self):
        mainWin = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
        time.sleep(30)
        self.driver.switch_to.window(mainWin)
        time.sleep(20)
        self.driver.find_element_by_xpath("//input[@value='Register']").click()



