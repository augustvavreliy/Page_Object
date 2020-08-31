import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('promo_offer_num', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
#@pytest.mark.xfail(promo_offer_num ="7")
def test_guest_can_add_product_to_basket(browser, promo_offer_num):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + promo_offer_num
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.check_product_name()
    page.check_product_price()