from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Env + Driver setup
load_dotenv()
driver = webdriver.Chrome()


# Login
driver.get("https://messenger.com")
time.sleep(1)
email_form = driver.find_element(By.ID, "email")
email_form.send_keys(os.getenv("USER_EMAIL"))

password_form = driver.find_element(By.ID, "pass")

password_form.send_keys(os.getenv("PASSWORD"))

login_button = driver.find_element(By.ID, "loginbutton")

login_button.click()

time.sleep(3)

# Message extraction

chat_pointers = driver.find_elements(By.XPATH, '//*[@id="jsc_c_c"]/div/div/*')

# WIP: does not handle scrolling through chat yet
unread_count = 0
for chat_pointer in chat_pointers:
    # click to get proper chat box to appear
    try:
        is_unread = chat_pointer.find_element(
            By.CSS_SELECTOR, '[aria-label="Mark as read"]'
        )
        print(is_unread)
        unread_count += 1
    except Exception as e:
        print("is read")

    time.sleep(1)
