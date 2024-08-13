from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()

try: 
    count=0
    chrome.get("http://uitestingplayground.com/dynamicid")
    button=chrome.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    for _ in range(3):
      button=chrome.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
      count=count+1
    print(count)
    sleep(5)
  
 
except Exception as ex:
    print(ex) 
finally:
    chrome.quit()