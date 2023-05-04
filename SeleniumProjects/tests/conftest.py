import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture(scope="class")
def initialise(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    desired_url = "https://rahulshettyacademy.com/angularpractice/"
    user_url = driver.current_url
    if desired_url == user_url:
        print("Url verified")
    else:
        print("Url is wrong")
    driver.implicitly_wait(4)
    request.cls.driver = driver
    yield
    driver.close()
