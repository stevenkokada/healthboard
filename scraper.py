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

for chat_pointer in chat_pointers[:1]:
    # click to get proper chat box to appear
    chat_pointer.click()
    print("HERE")
    # search updated html for chat history
    loaded_chat = driver.find_element(By.XPATH, '//*[@id="jsc_c_1t"]')

    loaded_chat_rows = loaded_chat.find_elements(By.XPATH, '//*[@role="row"]')

    for row in loaded_chat_rows:
        print(row.text)

    time.sleep(10)
