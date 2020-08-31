from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.XPATH, "//span[@class='btn-group']/a")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form button")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BOOK_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    PRICE_MESSAGE = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main")
    BOOK_PRICE = (By.CSS_SELECTOR, ".price_color")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")