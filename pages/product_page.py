from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def add_product_in_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def check_product_name(self):
        alert_text = self.browser.find_element(*ProductPageLocators.BOOK_MESSAGE).get_attribute("innerText") 
        product_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).get_attribute("innerText")
        assert alert_text in product_name, f"Product name should be: {product_name}, contains : {alert_text}"
    
    def check_product_price(self):
        alert_text = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).get_attribute("innerText") 
        product_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).get_attribute("innerText")
        assert alert_text in product_price, f"Product price should be: {product_price}, contains : {alert_text}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
    
    def should_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message NOT is disappeared, but should"