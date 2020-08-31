from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self, email, password):
        input = self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_EMAIL)
        input.send_keys(email)
        input = self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_PASSWORD)
        input.send_keys(password)
        input = self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_PASSWORD_CONFIRM)
        input.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        button.click()
