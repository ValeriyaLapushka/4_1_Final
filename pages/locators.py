from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
	
class LoginPageLocators(object):
	LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
	REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
	
class AddProduct(object):
	ADD_PRODUCT = (By.ID,"add_to_basket_form")
	BOOK_NAME = (By.TAG_NAME,"h1")
	BOOK_ALERT_NAME = (By.CSS_SELECTOR,"div.alertinner strong")
	
class NotBeSuccess(object):
	SUCCESS_ADD_PRODUCT = (By.PARTIAL_LINK_TEXT, 'has been added to your basket')
	
class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")