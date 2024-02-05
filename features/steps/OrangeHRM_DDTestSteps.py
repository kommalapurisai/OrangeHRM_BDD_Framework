import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
@given(u'I Lunch My Browser')
def step_impl(context):
    context.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


@when(u'I Open OrangeHRMLogIn Page')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.driver.maximize_window()
    time.sleep(5)


@when(u'I Entered username "{user}" and "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element(By.NAME, "username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)


@when(u'I Click on LogIn button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)


@then(u'Verify Profile is present or not')
def step_impl(context):
    try:
        profile = context.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").is_displayed()
        assert profile == True, "Test passed"
    except:
        context.driver.close()
        assert False," Test Failed"