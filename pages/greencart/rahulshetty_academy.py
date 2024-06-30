import time

from selenium.webdriver.common.by import By

from pages.basic_actions import BasicActions


class RahulShettyAcademy(BasicActions):
    login_button = (By.LINK_TEXT, 'Practice')
    home_page_link = (By.XPATH, "(//a[text() = 'Home'])[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_limited_offer_website_is_displayed(self):
        self.log_my_keyword_name_and_argument()
        self.select_tab_by_index(2)
        time.sleep(5)
        self.wait_for_element_to_be_visible(self.home_page_link)

    def validate_limited_offer_title(self):
        title = self.get_window_title()
        print(title)
        assert title == "Selenium, API Testing, Software Testing & More QA Tutorials | Rahul Shetty Academy"
        time.sleep(5)
