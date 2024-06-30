from selenium.webdriver.common.by import By

from pages.basic_actions import BasicActions


class GreenCartHomePage(BasicActions):
    """Link text"""
    limited_offer_link = (By.XPATH, "//div[@class='cart']/child::a[1]")
    search_input_button = (By.XPATH, "//input[@class = 'search-keyword']")
    add_to_cart_button = (By.XPATH, "//button[text() = 'ADD TO CART']")
    cart_icon = (By.CSS_SELECTOR, "a[class = 'cart-icon']")
    proceed_to_checkout_button = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_limited_offer_link_present(self):
        self.log_my_keyword_name_and_argument()
        self.wait_for_objects(self.limited_offer_link)
        self.get_web_element(self.limited_offer_link).is_displayed()
        self.get_attribute(self.limited_offer_link,'href')

    def select_limited_offer_link(self):
        self.log_my_keyword_name_and_argument()
        self.click_me(self.limited_offer_link)

    def search_items_by_name(self):
        self.click_me(self.search_input_button)
        self.type_words(self.search_input_button,"brocolli")

    def add_item_to_cart(self):
        self.click_me(self.add_to_cart_button)
        self.click_me(self.cart_icon)
        self.click_me(self.proceed_to_checkout_button)






