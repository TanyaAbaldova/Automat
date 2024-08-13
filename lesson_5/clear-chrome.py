from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()

try: 
    
    chrome.get("https://the-internet.herokuapp.com/inputs")
    vvod=chrome.find_element(By.TAG_NAME, "input")
    vvod.send_keys("1000")
    sleep(5)
    vvod.clear()
    sleep(5)
    vvod.send_keys("999")
    sleep(5)
    
 
except Exception as ex:
    print(ex) 
finally:
    chrome.quit()