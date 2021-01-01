from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from selenium.webdriver.support.ui import WebDriverWait
import time
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//*[@id='navbar-inverse-collapse']/div/div/a"
    _email_field = "//*[@id='email']"
    _password_field = "//*[@id='password']"
    _login_button = "//*[@id='page']/div[2]/div/div/div/div/form/div[4]/div[1]/input"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        time.sleep(1)
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)

        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[@id='dropdownMenu1']/img",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Your username or password is invalid. Please try again.')]",
                                       locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def verifyLoginTitle(self):
        return self.verifyPageTitle("All Courses")
        # if "google" in self.getTitle():
        #     # All Courses
        #     return True
        # else:
        #     return False
