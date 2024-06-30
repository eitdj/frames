from selenium.webdriver.common.by import By

from pages.basic_actions import BasicActions


class CountryPage(BasicActions):
    select_dropdown = (By.XPATH, "//div[@class = 'wrapperTwo']/child::div/child::select")
    agree_checkbox = (By.CLASS_NAME, "chkAgree")
    proceed_button = (By.XPATH, "//button[text()='Proceed']")
    order_success = (By.XPATH, "//span[text() ='Thank you, your order has been placed successfully ']")
    order_success_message = "Thank you, your order has been placed successfully "

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_the_country_from_dropdown(self):
        self.wait_for_objects(self.select_dropdown)
        self.select_from_list_by_value(self.select_dropdown, "India")

    def select_terms_and_condition_checkbox(self):
        self.get_check_box_value(self.agree_checkbox)
        self.set_check_box_value(self.agree_checkbox)

    def select_proceed_option(self):
        self.click_me(self.proceed_button)

    def validate_the_order_message(self):
        received_message = self.get_text_of_the_object(self.order_success_message)
        assert self.order_success_message == received_message
