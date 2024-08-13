from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()

try: 
    
    firefox.get("https://the-internet.herokuapp.com/login")
    login=firefox.find_element(By.ID, "username")
    password=firefox.find_element(By.ID, "password")
    button=firefox.find_element(By.TAG_NAME, "button")
    login.send_keys("tomsmith")
    sleep(5)
    password.send_keys("SuperSecretPassword!")
    sleep(5)
    button.click()
    sleep(5)
except Exception as ex:
    print(ex) 
finally:
    firefox.quit()