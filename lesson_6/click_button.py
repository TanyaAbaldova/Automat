from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome = webdriver.Chrome()

try: 
    chrome.get("http://uitestingplayground.com/ajax")

    add_button = chrome.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
    wait = WebDriverWait (chrome, 16).until( EC.visibility_of_element_located((By.CSS_SELECTOR, '.bg-success'))).text
    print(wait)



except Exception as ex:
    print(ex) 
finally:
    chrome.quit()