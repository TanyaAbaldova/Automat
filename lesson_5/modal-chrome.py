from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

chrome = webdriver.Chrome()

try: 
    
    chrome.get("https://the-internet.herokuapp.com/entry_ad")
    window=WebDriverWait(chrome,10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    close=WebDriverWait(chrome,1).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "modal-footer")))
    close.click()
    sleep(10)
    
 
except Exception as ex:
    print(ex) 
finally:
    chrome.quit()