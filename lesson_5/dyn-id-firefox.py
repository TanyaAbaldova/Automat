from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()

try: 
    count=0
    firefox.get("http://uitestingplayground.com/dynamicid")
    button=firefox.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    for _ in range(3):
      button=firefox.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
      count=count+1
    print(count)
    sleep(5)
  
 
except Exception as ex:
    print(ex) 
finally:
    firefox.quit()