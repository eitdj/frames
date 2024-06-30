import pytest

from pages.greencart.cart_page import CartPage
from pages.greencart.country_page import CountryPage
from pages.greencart.greencart_homepage import GreenCartHomePage
from pages.greencart.rahulshetty_academy import RahulShettyAcademy
from tests.conftest import open_browser_test_startup


class TestLimitedOffer:
    def test_limited_offer_link(self,open_browser_test_startup):
        green_home = GreenCartHomePage(self.driver)
        green_home.is_limited_offer_link_present()
        green_home.select_limited_offer_link()
        shetty_academy = RahulShettyAcademy(self.driver)
        shetty_academy.is_limited_offer_website_is_displayed()
        shetty_academy.validate_limited_offer_title()

    def test_place_the_order_successfully(self,open_browser_test_startup):
        green_home = GreenCartHomePage(self.driver)
        green_home.search_items_by_name()
        green_home.add_item_to_cart()
        cart_page = CartPage(self.driver)
        cart_page.place_the_order_of_the_item()
        country_page = CountryPage(self.driver)
        country_page.select_the_country_from_dropdown()
        country_page.select_terms_and_condition_checkbox()
        country_page.select_proceed_option()
        country_page.validate_the_order_message()

    def test_validate_invalid_promo_code_message(self,open_browser_test_startup):
        green_home = GreenCartHomePage(self.driver)
        green_home.search_items_by_name()
        green_home.add_item_to_cart()
        cart_page = CartPage(self.driver)
        cart_page.apply_promo_code()
        cart_page.validate_invalid_message()





