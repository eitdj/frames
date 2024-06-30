from selenium.webdriver.common.by import By

from pages.basic_actions import BasicActions


class CartPage(BasicActions):
    place_order_button = (By.XPATH, "//button[text()='Place Order']")
    promo_code_input = (By.CLASS_NAME, "promoCode")
    promo_code_apply = (By.CLASS_NAME, "promoBtn")
    promo_info_message = (By.CLASS_NAME, "promoInfo")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def place_the_order_of_the_item(self):
        self.log_my_keyword_name_and_argument()
        self.wait_for_objects(self.place_order_button)
        self.click_me(self.place_order_button)

    def apply_promo_code(self):
        self.get_web_element(self.promo_code_input)
        self.type_words(self.promo_code_input,"Rahul")
        self.click_me(self.promo_code_apply)

    def validate_invalid_message(self):
        self.wait_for_element_to_be_visible(self.promo_info_message)
        element = self.get_text_of_the_object()
        assert element == self.promo_info_message




