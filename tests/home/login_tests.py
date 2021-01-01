from selenium import webdriver
from pages.home.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from utilities.teststatus import TestStatus
import unittest
import pytest
import time


class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result1, "Title Verified")
        result2 = self.lp.verifyLoginTitle()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@mail.com", "abcabcabc")
        time.sleep(2)
        result = self.lp.verifyLoginFailed()
        assert result == True
