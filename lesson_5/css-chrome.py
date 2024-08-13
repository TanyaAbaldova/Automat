from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()

try: 
    count=0
    chrome.get("http://uitestingplayground.com/classattr")
    
    for _ in range(3):
      button=chrome.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
      count=count+1
      chrome.switch_to.alert.accept()
    print(count)
    sleep(5)
  
 
except Exception as ex:
    print(ex) 
finally:
    chrome.quit()