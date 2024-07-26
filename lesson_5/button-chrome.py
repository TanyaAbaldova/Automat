from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()

try: 
    chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")

    for _ in range(5):
        add_button = chrome.find_element(By.XPATH, '//button[text()="Add Element"]').click()
        
    
        delete_chrome = chrome.find_elements(By.XPATH,'//button[text()="Delete"]')

    print(f"Хром {len(delete_chrome)}")
    sleep(5)

except Exception as ex:
    print(ex) 
finally:
    chrome.quit()