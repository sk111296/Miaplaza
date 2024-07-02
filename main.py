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

#open browser
driver = webdriver.Chrome()

#navigate to https://miacademy.co/#/
driver.get("https://miacademy.co/#/")
time.sleep(10)


