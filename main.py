"""Practical Task
Automate the following flows using the C# programming language and any automation framework:
navigate to https://miacademy.co/#/
navigate to MiaPrep Online High School through the link on banner
apply to MOHS
fill in the Parent Information
proceed to Student Information page
STOP YOUR TEST HERE"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#open browser
driver = webdriver.Chrome()

#navigate to https://miacademy.co/#/
driver.get("https://miacademy.co/#/")
time.sleep(5)

#navigate to MiaPrep Online High School through the link on banner
link = (driver.find_element(By.LINK_TEXT, 'Online High School'))
link.click()
time.sleep(5)

# apply to MOHS/click on Apply to our school button on the banner
apply_button_xpath = ("/html//main[@id='main']/div[@class='content-wrap']/article/div[@class='entry-content-wrap']/div/div[2]/div//a"
                      "[@href='https://forms.zohopublic.com/miaplazahelp/form/MOHSInitialApplication/formperma/okCyt4yyq39rZvSBXB9FSjDeek1ilbRVK1iNCK--3K8']")
apply_button_locator = driver.find_element(By.XPATH, apply_button_xpath)
apply_button_locator.click()
time.sleep(5)