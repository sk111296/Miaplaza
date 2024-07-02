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
from selenium.webdriver.support.select import Select

#open browser
driver = webdriver.Chrome()
driver.maximize_window()

#navigate to https://miacademy.co/#/
driver.get("https://miacademy.co/#/")
#time.sleep(2)

#navigate to MiaPrep Online High School through the link on banner
link = (driver.find_element(By.LINK_TEXT, 'Online High School'))
link.click()
#time.sleep(2)

# apply to MOHS/click on Apply to our school button on the banner
apply_button_xpath = ("/html//main[@id='main']/div[@class='content-wrap']/article/div[@class='entry-content-wrap']/div/div[2]/div//a"
                      "[@href='https://forms.zohopublic.com/miaplazahelp/form/MOHSInitialApplication/formperma/okCyt4yyq39rZvSBXB9FSjDeek1ilbRVK1iNCK--3K8']")
apply_button_locator = driver.find_element(By.XPATH, apply_button_xpath)
apply_button_locator.click()
#time.sleep(2)

#fill in the Parent Information
#enter parent name
first_name = driver.find_element(By.XPATH, "//li[@id='Name-li']/div[@class='tempContDiv twoType']/div/span[1]/input[@name='Name']")
first_name.send_keys("Max")

#enter last name
last_name = driver.find_element(By.XPATH, "//li[@id='Name-li']/div[@class='tempContDiv twoType']/div/span[2]/input[@name='Name']")
last_name.send_keys("Mustermann")

#enter email id
email_id = driver.find_element(By.ID, "Email-arialabel")
email_id.send_keys("max.mustermann@email.com")
time.sleep(2)

#enter mobile number


#select value from drop down for additional parent informaiton
drop_down = driver.find_element(By.ID, "Dropdown-arialabel")
values=Select(drop_down)
values.select_by_visible_text("Yes")
time.sleep(4)






#driver.close()





