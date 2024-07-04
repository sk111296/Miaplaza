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


#navigate to MiaPrep Online High School through the link on banner
link = (driver.find_element(By.LINK_TEXT, 'Online High School'))
link.click()


# apply to MOHS/click on Apply to our school button on the banner
apply_button_xpath = ("/html//main[@id='main']/div[@class='content-wrap']/article/div[@class='entry-content-wrap']/div/div[2]/div//a"
                      "[@href='https://forms.zohopublic.com/miaplazahelp/form/MOHSInitialApplication/formperma/okCyt4yyq39rZvSBXB9FSjDeek1ilbRVK1iNCK--3K8']")
apply_button_locator = driver.find_element(By.XPATH, apply_button_xpath)
apply_button_locator.click()

time.sleep(2)

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
time.sleep(1)

"""select country code
CountryCode = driver.find_element(By.CLASS_NAME, "selected-dial-code")
CountryCode.click()
time.sleep(5)
Code = driver.find_element(By.XPATH, "//div[@class='intl-tel-input iti-container']/ul[@class='country-list']/li[@class='country highlight']")
Code.click()
time.sleep(1)"""

#enter mobile number
number = driver.find_element(By.ID, "PhoneNumber")
number.send_keys("1766767432")

#select value from drop down for additional parent informaiton
drop_down = driver.find_element(By.ID, "Dropdown-arialabel")
values=Select(drop_down)
values.select_by_visible_text("Yes")
time.sleep(2)

#enter second parent information
secparent_fname = driver.find_element(By.XPATH, "//div[@id='formBodyDiv']/ul[1]/li[7]//div[@class='nameWrapper']/span[1]/input[@name='Name1']")
secparent_fname.send_keys("Michelle")

time.sleep(1)

secparent_lname = driver.find_element(By.XPATH, "//div[@id='formBodyDiv']/ul[1]/li[7]//div[@class='nameWrapper']/span[2]/input[@name='Name1']")
secparent_lname.send_keys("Mustermann")

time.sleep(1)

secparent_emailID = driver.find_element(By.ID,"Email1-arialabel")
secparent_emailID.send_keys("MIchelle.Mustermann@email.com")

time.sleep(1)

secparent_phonenum = driver.find_element(By.NAME, "PhoneNumber1")
secparent_phonenum.send_keys("1766767454")
time.sleep(2)

#to scroll page down
driver.execute_script("scrollBy(0,100)")

#How did you hear about us? (Select all checkbox that apply)
checkbox1 = driver.find_element(By.XPATH, "//li[@id='Checkbox-li']//div[@role='group']/span[1]/label[@class='checkChoice cusChoiceLabel']")
checkbox1.click()

time.sleep(1)

checkbox2 = driver.find_element(By.XPATH, "//li[@id='Checkbox-li']//div[@role='group']/span[2]/label[@class='checkChoice cusChoiceLabel']")
checkbox2.click()

time.sleep(1)

checkbox3 = driver.find_element(By.XPATH, "//li[@id='Checkbox-li']//div[@role='group']/span[3]/label[@class='checkChoice cusChoiceLabel']")
checkbox3.click()


time.sleep(2)

#to scroll page down
driver.execute_script("scrollBy(0,1000)")

time.sleep(1)

#What is your preferred start date? *
Calendar = driver.find_element(By.ID, "Date-date")
Calendar.click()
time.sleep(4)
Date = driver.find_element(By.ID, "ui-datepicker-div")
Start_date = driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']/table[@class='ui-datepicker-calendar']/tbody/tr[4]/td[1]/a[@href='#']")
Start_date.click()

time.sleep(3)

#click on next button to navigate to student information page
next_button = driver.find_element(By.XPATH, "/html//li[@id='formAccess']//div[@class='inlineBlock nextAlign']/button[@type='button']")
next_button.click()

time.sleep(2)

#close the browser
driver.close()





