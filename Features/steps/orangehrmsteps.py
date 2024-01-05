from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Firefox()

@when('open orange HRM home page')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then('verify that logo present on page')
def step_impl(context):
    status=context.driver.find_element(By.XPATH("//img[@alt='company-branding']")).is_displayed()
    assert status is True
@then('close browser')
def step_impl(context):
    context.driver.close()