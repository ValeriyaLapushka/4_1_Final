from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.product_page import PageObject
from selenium.webdriver.common.by import By
import time
import pytest


#@pytest.mark.parametrize('link',['1','2','7','3','4','5','6','8','9','0'])
#def test_guest_can_add_product_to_cart(browser, link):
#	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}'.format(link)
#	page = PageObject(browser, link)
#	page.open()
#	page.guest_can_add_product()
#	page.solve_quiz_and_get_code()
#	page.check_name()


#def test_guest_can_add_product_to_cart_1(browser):
#	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
#	page = PageObject(browser, link)
#	page.open()
#	page.guest_can_add_product()
#	page.solve_quiz_and_get_code()
#	page.check_name()


# def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    # page = PageObject(browser, link)
    # page.open()
    # page.guest_can_add_product()	
    # page.is_not_element_present()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()
	
	
	
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = BasePage(browser, link)
	page.open()
	login_page = page.go_to_login_page()
	login_page.should_be_login_link()

# def test_guest_cant_see_success_message(browser):
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    # page = PageObject(browser, link)
    # page.open()
    # page.is_not_element_present()


# def test_message_disappeared_after_adding_product_to_cart(browser):
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    # page = PageObject(browser, link)
    # page.open()
    # page.guest_can_add_product()
    # page.is_disappeared()
	
	
