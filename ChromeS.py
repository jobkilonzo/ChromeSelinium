from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://www.gmail.com")

element = driver.find_element_by_id("identifierId")

element.send_keys("your email")

element = driver.find_element_by_id("identifierNext")
element.click()
time.sleep(1)
element = driver.find_element_by_xpath(".//input[contains(@name, 'password')]")
element.send_keys("password")
element = driver.find_element_by_id("passwordNext")
element.click()
