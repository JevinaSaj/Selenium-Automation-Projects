import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

@pytest.fixture(scope="class")
def browser_invoke(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    desired_url = "https://www.saucedemo.com/"
    user_url = driver.current_url
    if desired_url == user_url:
        print("Url verified")
    else:
        print("Url is wrong")
    driver.implicitly_wait(4)
    request.cls.driver = driver
    # yield
    # driver.close()
