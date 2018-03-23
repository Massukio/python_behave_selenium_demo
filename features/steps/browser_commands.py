from behave import *
use_step_matcher("re")

@then("I print current url")
def step_impl(context):
    print(context.browser.current_url)

@step("I click ABOUT link")
def step_impl(context):
    context.browser.find_element_by_link_text("ABOUT").click()
    assert "ABOUT" in context.browser.title

@then("I click back on the browser")
def step_impl(context):
    context.browser.back()
    assert "Selenium" in context.browser.title

@step("I click forward on the browser")
def step_impl(context):
    context.browser.forward()
    assert "ABOUT" in context.browser.title

@step("I click refresh on the browser")
def step_impl(context):
    context.browser.refresh()

@step("print the name")
def step_impl(context):
    print(context.browser.name)
