from behave import *
from selenium import webdriver



@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('open register page')
def openRegPage(context):
    context.driver.get("http://demo.automationtesting.in/Index.html")


@then('verify on the register page')
def verifyPage(context):
    context.driver.find_element_by_id("btn2").click()


@then('close browser')
def closeBrowser(context):
    context.driver.close()