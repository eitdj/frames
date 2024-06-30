import pytest
from selenium import webdriver

from pages.basic_actions import BasicActions


# def open_browser_test_startup(request):
#     global driver
#     basic_action = BasicActions(driver = None)
#     basic_action.maximize_browser_window()
#     basic_action.open_my_browser()
@pytest.fixture(scope="class")
def open_browser_test_startup(request):
    # Initialize Chrome WebDriver without ChromeDriverManager
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Maximize window on startup
    driver = webdriver.Chrome(options=options)

    # Navigate to the initial URL or perform setup actions as needed
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

    # Assign the driver instance to the test class instance
    request.cls.driver = driver

    yield driver # Provide the driver instance to the tests

    # Teardown: Close the browser after all tests in the class complete
    driver.quit()




