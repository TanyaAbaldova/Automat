from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
chrome = webdriver.Chrome()

try: 
    chrome.get("http://uitestingplayground.com/textinput")
    text_field = WebDriverWait (chrome, 20).until(chrome.find_element(By.ID, "newButtonName").send_keys("SkyPro"))
    button = chrome.find_element(By.CSS_SELECTOR, ".btn btn-primary").click
    newtext = chrome.find_element(By.CSS_SELECTOR, "#updatingButton.btn.btn-primary").text
    print(newtext)
    



except Exception as ex:
    print(ex) 
finally:
    chrome.quit()