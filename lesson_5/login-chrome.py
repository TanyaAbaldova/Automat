from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()

try: 
    
    chrome.get("https://the-internet.herokuapp.com/login")
    login=chrome.find_element(By.ID, "username")
    password=chrome.find_element(By.ID, "password")
    button=chrome.find_element(By.TAG_NAME, "button")
    login.send_keys("tomsmith")
    sleep(5)
    password.send_keys("SuperSecretPassword!")
    sleep(5)
    button.click()
    sleep(5)
except Exception as ex:
    print(ex) 
finally:
    chrome.quit()