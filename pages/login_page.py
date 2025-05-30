from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login URL is incorrect"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(By.NAME, "registration-email")
        password_input1 = self.browser.find_element(By.NAME, "registration-password1")
        password_input2 = self.browser.find_element(By.NAME, "registration-password2")
        register_button = self.browser.find_element(By.NAME, "registration_submit")

        email_input.send_keys(email)
        password_input1.send_keys(password)
        password_input2.send_keys(password)
        register_button.click()