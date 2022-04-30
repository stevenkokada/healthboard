from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from database import write_unread_messages
import time
import os
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import datetime
# sometimes it takes selenium to start up
sleep(5)

# Env + Driver setup
load_dotenv()
driver = webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)


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

while True:
    time.sleep(30)
    scraped_messages = set()
    unread_count = 0
    unread_chat_names_elts = driver.find_elements(By.XPATH, '//*[@id="jsc_c_c"]/div/div/div[*]/div/div[1]/a/div[1]/div/div[2]/div/div/span/span')
    print("number of chats: ", len(unread_chat_names_elts))

    # If we aren't seeing any chat elements, something is wrong, exit the program
    if len(unread_chat_names_elts) == 0:
        driver.save_screenshot(f"screenshot-{int(time.time())}.png")
        break

    for chat_name_elt in unread_chat_names_elts:
        try:
            if int(chat_name_elt.value_of_css_property('font-weight')) > 500:
                unread_count += 1
                sender_name = chat_name_elt.get_attribute("innerText")
                scraped_messages.add(sender_name)
        except Exception as e:
            print("couldn't get chat name")

    print(f"is_unread: {unread_count} at {datetime.datetime.now()}")

    # Write to DB
    write_unread_messages(scraped_messages)
