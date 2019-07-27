from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from .locators import MainPageLocators, AddProduct, NotBeSuccess
from selenium.common.exceptions import NoAlertPresentException
import math



class PageObject(BasePage):
	def open(self):
		self.browser.get(self.url)


	def guest_can_add_product(self):
		add_product = self.browser.find_element(*AddProduct.ADD_PRODUCT)
		add_product.click()
		assert self.browser.switch_to.alert , 'Алерт не вылез'
		
		
	def check_name(self):
		book_alert_name = self.browser.find_element(*AddProduct.BOOK_ALERT_NAME).text
		book_name = self.browser.find_element(*AddProduct.BOOK_NAME).text
		assert  book_alert_name == book_name, 'Названия не совпадают'
		
		
		
	def should_be_login_link(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Ссылки нет"
			
	

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*NotBeSuccess.SUCCESS_ADD_PRODUCT), "Success message is presented, but should not be"
		
		
		
	def should_not_be_success_message_for_is_disappeared(self):
		assert self.is_disappeared(*NotBeSuccess.SUCCESS_ADD_PRODUCT), "Success message is presented, but should not be"
		
		

		
		
	


	   