from behave import given,when,then
from selenium import webdriver


@given(u'launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome("D:\drivers\chromedriver_win32\chromedriver.exe")


@when(u'open homepage')
def openPage(context):
    context.driver.get("https://444.hu/")

@then(u'verify that the logo present on the page')
def verifyLogo(context):
    status = context.driver.find_element("xpath",'//body/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/figure[1]/a[1]/img[1]').is_displayed()
    assert status is True

@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
