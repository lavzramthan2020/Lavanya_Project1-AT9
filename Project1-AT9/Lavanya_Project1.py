from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
import time

browser= webdriver.Chrome()
browser.maximize_window()
browser.get("https://opensource-demo.orangehrmlive.com/")


# Enter the username and Password
time.sleep(3)
browser.find_element(By.NAME, value="username").send_keys("Admin")
browser.find_element(By.NAME, value="password").send_keys("admin123")
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(3)

#Navigate to PIM
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(3)

#Click on Add button
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button/i').click()
time.sleep(3)

#Enter employee details
browser.find_element(By.NAME, value="firstName").send_keys("Lavanya")
#browser.find_element(By.NAME, value="middleName")
browser.find_element(By.NAME, value="lastName").send_keys("Ramar")
#browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input').send_keys("3960")
time.sleep(5)


#Click Save
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
time.sleep(5)

#Navigate to admin Section
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
time.sleep(5)

#Click on Add button
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
time.sleep(5)

#Enter Add User details
#UserRole
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]').click()
userrolelistbox=browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[@role="listbox"]')

actions=ActionChains(browser)
WebDriverWait(browser, 10).until(ec.visibility_of(userrolelistbox))
actions.move_to_element(userrolelistbox)
Role=browser.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[@role="listbox"]/div')
print(len(Role))
for i in Role:
    print(i.text+ "**")
actions.move_to_element(Role[1]).click().perform()

#Employee Name
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys("Lavanya  Ramar")
time.sleep(2)
actions.move_to_element(browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]'))
time.sleep(5)
Emp_Name=browser.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]/div')
time.sleep(5)
for i in Emp_Name:
    if i.text == "Lavanya Ramar":
        i.click()
        break

#Status
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]').click()
time.sleep(5)
actions.move_to_element(browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[@role="listbox"]'))
time.sleep(5)
Status=browser.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[@role="listbox"]/div')
for i in Status:
    if i.text=="Enabled":
        i.click()
        break
        
        
time.sleep(5)

#UserName
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys("Guvizen@78")

#Password
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("Admin@123")

#Confirm Password
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("Admin@123")
time.sleep(5)

#Click Save
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()
time.sleep(10)


#Once the user is created search for the user in admin section

#Navigation to Admin Section
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
time.sleep(5)

#Enter Username details
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("Guvizen@78")
time.sleep(5)


#click on Search
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()

time.sleep(10)

#Logout
browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p').click()
time.sleep(3)
browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
time.sleep(5)

#Relogin
browser.find_element(By.NAME, value="username").send_keys("Guvizen@78")
browser.find_element(By.NAME, value="password").send_keys("Admin@123")
browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(10)










