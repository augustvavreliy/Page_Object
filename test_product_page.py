import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

@pytest.mark.user_register
class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "fdyhtijt&ee"
        login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
    
    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_in_basket()
        #page.solve_quiz_and_get_code()
        page.check_product_name()
        page.check_product_price()

@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer_num', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
@pytest.mark.xfail(promo_offer_num ="7")
def test_guest_can_add_product_to_basket(browser, promo_offer_num):
    link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + promo_offer_num
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.check_product_name()
    page.check_product_price()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.should_message_disappeared_after_adding_product_to_basket()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_no_items()
    page.should_be_message_empty_basket()