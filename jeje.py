from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 7)
url = """https://commerce.adobe.com/checkout/email/?items%5B0%5D%5Bid%5D=08823B2E8361CE018F9A2C51CF489283&items%5B0%5D%5Bq%5D=1&items%5B0%5D%5Bcs%5D=1&items%5B0%5D%5Bcv%5D=%5Bobject%20Object%5D&cli=creative&co=US&lang=es&oco=MX&fr=v1"""
driver.get(url)
a = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qe-id='user-email-input']")))
a.send_keys("ANSDJLAHSadsasdDJAHSDJK@gmail.com")
b = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='action-button-email']")))
b.click()
c = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='creditCardNumber']")))
c.send_keys("4571736075448381")
ad = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@data-qid='creditCardExpiryMonth']")))
ad.click()
d = wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@data-value='3']")))
d.click()
ac = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@data-qid='creditCardExpiryYear']")))
ac.click()
e = wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@data-value='2021']")))
e.click()
f = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='firstName']")))
f.send_keys("olaytuxd")
sleep(2)
g = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='lastName']")))
g.send_keys("america")
sleep(2)
h = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='street1']")))
h.send_keys("4543 Street Rd")
sleep(2)
aa = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='postalCode']")))
aa.send_keys("18976")
asd = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='companyName']")))
asd.send_keys("")
sleep(2)
bb = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@data-qe-id='action-button-payment-popup']")))

bb.click()
try:

	kaka = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@data-qid='custom-error-alert-box']")))
	print("chale esta die unu")
except:
	print("live")

print("bruh momento xd")

