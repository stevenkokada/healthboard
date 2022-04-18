from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from database import write_unread_messages
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

time.sleep(5)

# Message extraction

chat_pointers = driver.find_elements(By.XPATH, '//*[@id="jsc_c_c"]/div/div/*')

# WIP: does not handle scrolling through chat yet
unread_count = 0
# for chat_pointer in chat_pointers:
#     # click to get proper chat box to appear
#     try:
#         is_unread = chat_pointer.find_element(
#             By.CSS_SELECTOR, '[aria-label="Mark as read"]'
#         )
        
#         unread_count += 1

#     except Exception as e:
#         print("is read")

#     time.sleep(1)

scraped_messages = set()

unread_chat_names_elts = driver.find_elements(By.XPATH, '//*[@id="jsc_c_c"]/div/div/div[*]/div/div[1]/a/div[1]/div/div[2]/div/div/span/span')
for chat_name_elt in unread_chat_names_elts:
    try:
        if int(chat_name_elt.value_of_css_property('font-weight')) > 500:
            unread_count += 1
            sender_name = chat_name_elt.get_attribute("innerText")
            scraped_messages.add(sender_name)
    except Exception as e:
        print("couldn't get chat name")

print(f"is_unread: {unread_count}")
# Write to DB


write_unread_messages(scraped_messages)
