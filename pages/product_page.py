from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from .locators import MainPageLocators, AddProduct, NotBeSuccess
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
		
		
		
	def solve_quiz_and_get_code(self):
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.browser.switch_to.alert
			print("Your code: {}".format(alert.text))
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")
			
	

	#def should_not_be_success_message(self):
	#	
	##	assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
		
		
		
		
		
	# def is_disappeared(self, how, what, timeout=4):
		# try:
			# WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located(how, what))
		# except TimeoutException:
			# return False

		# return True	
		
		
	# def is_not_element_present(self,how, what, timeout=4):
		# try:
			# WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(By.PARTIAL_LINK_TEXT, 'has been added to your basket'))
		# except TimeoutException:
			# return True

		# return False	
		
		
	


	   