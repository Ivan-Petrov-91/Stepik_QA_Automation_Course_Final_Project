from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'Items are present in basket, but should not be'

    def empty_basket_message_is_present(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        empty_basket_message_text = empty_basket_message.text
        assert "empty" in empty_basket_message_text, 'Basket is not empty'
