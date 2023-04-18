from time import sleep
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Windows/System32/chromedriver_win32/chromedriver.exe")
#driver.get('https:www.sport5.co.il')
driver.get("C:/Users/shaar/Desktop/Devops course/Lesson 4/tip_calc/index.html")
billamt = driver.find_element(by="id", value="billamt")
billamt.send_keys("100")
s = driver.find_element(by="xpath", value='//*[@id=\"serviceQual\"]/option[5]')
s.click()
peopleamt = driver.find_element(by="id", value="peopleamt")
peopleamt.send_keys("5")
driver.find_element(by="id", value="calculate").click()
tip = (driver.find_element(by="id", value="tip")).text
print(tip)


s.click()
sleep(10)
driver.close()
