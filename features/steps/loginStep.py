from selenium import webdriver
from behave import *
from data.config import TestData
import time

@given('launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('open the perpus website')
def step_impl(context):
    context.driver.get(TestData.URL)


@then('the website has been opened')
def step_impl(context):
    assert context.driver.find_element_by_xpath('//*[@id="navbar-toggle-collapse"]/ul[2]/li/a').is_displayed()
    


@then('click menu login')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="navbar-toggle-collapse"]/ul[2]/li/a').click()
    time.sleep(1)


@then(u'input the username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element_by_id('email').send_keys(username)
    context.driver.find_element_by_id('password').send_keys(password)


@then(u'input the username "{username}"')
def step_impl(context, username):
    context.driver.find_element_by_id('email').send_keys(username)


@then(u'input the password "{password}"')
def step_impl(context, password):
    context.driver.find_element_by_id('password').send_keys(password)


@then(u'click th login button')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="bv-modal-example___BV_modal_body_"]/div[2]/form/div[3]/button/span').click()
    time.sleep(2)

@then(u'login is successfull')
def step_impl(context):
    time.sleep(2)


@then(u'close browser')
def step_impl(context):
    context.driver.close()


@then(u'login is failed and error message invalid username is displayed')
def step_impl(context):
    assert context.driver.find_element_by_xpath('//*[@id="bv-modal-example___BV_modal_body_"]/div[2]/form/div[1]/p').text == "Email/Username Salah"

    time.sleep(1)

@then(u'login is failed and error message invalid password is displayed')
def step_impl(context):
    assert context.driver.find_element_by_xpath('//*[@id="bv-modal-example___BV_modal_body_"]/div[2]/form/div[2]/p').text == "Password Salah"

    time.sleep(1)


@then(u'login is failed and error message empty username is displayed')
def step_impl(context):
    assert context.driver.find_element_by_xpath('//*[@id="bv-modal-example___BV_modal_body_"]/div[2]/form/div[1]/p').text == "Email/Username tidak boleh kosong"
    time.sleep(1)


@then(u'login is failed and error message empty password is displayed')
def step_impl(context):
    assert context.driver.find_element_by_xpath('//*[@id="bv-modal-example___BV_modal_body_"]/div[2]/form/div[2]/p').text == "Password tidak boleh kosong"
    time.sleep(1)
