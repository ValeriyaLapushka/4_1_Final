from pages.base_page import BasePage


class LoginPage(BasePage):
	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):
		assert 'login' in str(self.current_url), "Что ты блин ищеiь там"
		
		
		

	def should_be_login_form(self):
		assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Форма для логина не найдена'



	def should_be_register_form(self):
		assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Форма для регистрации не найдена'

