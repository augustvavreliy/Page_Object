from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_no_items(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Should be empty, but not"

    def should_be_message_empty_basket(self):
        text = self.browser.find_element(
            *BasketPageLocators.EMPTY_MESSAGE).text
        assert text in "Your basket is empty. Continue shopping", f"Product price should be: Your basket is empty , contains : {text}"