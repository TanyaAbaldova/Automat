from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()

try: 
    firefox.get("https://the-internet.herokuapp.com/add_remove_elements/")

    for _ in range(5):
        add_button = firefox.find_element(By.XPATH, '//button[text()="Add Element"]').click()
        
        delete_firefox = firefox.find_elements("xpath",'//button[text()="Delete"]')

    print(f"Фаерфокс {len(delete_firefox)}")
    sleep(5)

except Exception as ex:
    print(ex) 
finally:
    firefox.quit()