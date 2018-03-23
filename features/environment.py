from selenium import webdriver

def before_scenario(context, scenario):
    if "no_browser" not in scenario.effective_tags:
        context.browser = webdriver.Firefox()
        context.browser.maximize_window()


def after_scenario(context, scenario):
    if "no_browser" not in scenario.effective_tags:
        context.browser.quit()
