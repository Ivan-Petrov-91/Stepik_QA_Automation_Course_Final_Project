from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        product_name = self.get_product_name()
        product_price = self.get_product_price()
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_button.click()
        BasePage.solve_quiz_and_get_code(self)
        product_name_in_basket = self.get_product_name_in_basket()
        basket_total = self.get_basket_total()
        assert product_name == product_name_in_basket, 'Invalid product name'
        assert product_price == basket_total, 'Invalid basket total'

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text
        return product_name_text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_text = product_price.text
        return product_price_text

    def get_product_name_in_basket(self):
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        product_name_in_basket_text = product_name_in_basket.text
        return product_name_in_basket_text

    def get_basket_total(self):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        basket_total_text = basket_total.text
        return basket_total_text
