from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://www.facebook.com')

email = driver.find_element_by_id('email')
email.send_keys('your_user_email')


password = driver.find_element_by_id('pass')
password.send_keys('your_password')

log_in_button = driver.find_element_by_id('loginbutton')
log_in_button.click()

time.sleep(5)

search_query=driver.find_element_by_name('q')
search_query.send_keys('"Web development jobs"')
time.sleep(5)
search_query.send_keys(Keys.RETURN)
search_query.click()
