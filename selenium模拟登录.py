from selenium import webdriver
from selenium.webdriver.common.keys import Keys



browser = webdriver.Chrome()  
browser.get('http://www.imooc.com/user/newlogin/')


browser.find_element_by_xpath("//input[@name='email']").send_keys("13255290027")

browser.find_element_by_xpath("//input[@name='password']").send_keys("132csvcsxcs156")

browser.find_element_by_xpath("//input[@value='登录']").click()

browser.find_element_by_xpath("//div[@id='login-area']/ul/li[3]/a/i").click()



