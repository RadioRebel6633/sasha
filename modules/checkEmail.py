import time
from selenium import webdriver 
def openEmail():
	browser = webdriver.Chrome('C:/Users/cody/Desktop/test/modules/chromedriver.exe')
	browser.maximize_window()
	browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

	email_field = browser.find_element_by_id('identifierId')
	email_field.clear()
	email_field.send_keys('14braunc@gmail.com')

	submit_button = browser.find_element_by_id('identifierNext')
	submit_button.click()
	time.sleep(3)
	pass_field = browser.find_element_by_name('password')
	pass_field.clear()
	pass_field.send_keys('Lrawlins')
	pass_sub_button = browser.find_element_by_id('passwordNext')
	pass_sub_button.click()