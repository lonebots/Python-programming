from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#driver/browser
driver = webdriver.Chrome("C:/chrome-driver/chromedriver.exe")

#opening whatsappweb
driver.get("https://web.whatsapp.com")
wait=WebDriverWait(driver,600)

target='"-"'#name of receiver (replace -)
string=" - " #message (replace -)

#setting the arguement and getting it using the xpath of the span
x_arg='//span[contains(@title,'+target+')]'
target=wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
target.click()

input_box = driver.find_element_by_class_name("DuUXI")
input_box.send_keys(string+Keys.ENTER)
