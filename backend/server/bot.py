from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

# sometimes it takes selenium to start up
sleep(5)

driver = webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
driver.get('https://googlg\e.com')
driver.save_screenshot('screenshot.png')