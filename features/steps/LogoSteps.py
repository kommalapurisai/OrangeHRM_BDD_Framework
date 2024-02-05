import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
@given(u'I lunch chrome browser')
def step_impl(context):
    context.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


@when(u'I open OrangeHRM Home Page')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()
    time.sleep(5)


@then(u'must the logo present on page')
def step_impl(context):
    context.logo=context.driver.find_element(By.XPATH,"//div[@class='orangehrm-login-logo']//img")
    if context.logo.is_displayed()==True:
        assert True
    else:
        assert False
