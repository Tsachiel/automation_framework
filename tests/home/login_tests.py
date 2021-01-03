from selenium import webdriver
from pages.home.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
from ddt import ddt, data, unpack
from utilities.readdata import getCSVData

@ddt
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
    @data(*getCSVData("testdata.csv"))
    @unpack
    def test_invalidLogin(self,user,pw):
        self.lp.login(user, pw)
        time.sleep(1)
        result = self.lp.verifyLoginFailed()
        assert result == True
