from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

elem = driver.find_element(By.CLASS_NAME, "KzDlHZ")
print(elem.get_attribute("outerHTML"))

time.sleep(10)
driver.close()