#import statements
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Opens Flipkart's search results for the given link
driver = webdriver.Chrome()
# print the 
for i in range(1,20):
    driver.get(f"https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page = {i}")

    elems = driver.find_elements(By.CLASS_NAME, "KzDlHZ")
    print(f"{len(elems)} items found")
    print(elems)
    for elem in elems:
        print(elem.text)
    #print(elem.get_attribute("outerHTML"))
    #print(elem.text)

    time.sleep(1)
driver.close()