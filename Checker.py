from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.action_chains import ActionChains
import random
from time import sleep
import colorama
from colorama import Fore,Back,init
init()

datos= []
name = []
def goto(linenum):
    global line
    line = linenum


class file():
	def file(self,nombre):
		if ".txt" in nombre:
			file = open(nombre).readlines()
			file = [a.rstrip() for a in file]
			for lines in file:
				datos.append(lines)
			name.append(nombre)
		else:
			file = open(nombre+".txt").readlines()
			file = [a.rstrip() for a in file]
			for lines in file:
				datos.append(lines)
			name.append(nombre+".txt")


banner = """
..######..##.....##.########..######..##....##.########.########.....########..########..##.....##..######..
.##....##.##.....##.##.......##....##.##...##..##.......##.....##....##.....##.##.....##.##.....##.##....##.
.##.......##.....##.##.......##.......##..##...##.......##.....##....##.....##.##.....##.##.....##.##.......
.##.......#########.######...##.......#####....######...########.....########..########..#########.##...####
.##.......##.....##.##.......##.......##..##...##.......##...##......##........##.....##.##.....##.##....##.
.##....##.##.....##.##.......##....##.##...##..##.......##....##.....##........##.....##.##.....##.##....##.
..######..##.....##.########..######..##....##.########.##.....##....##........########..##.....##..######..
"""
menu ="""

____________________________________________________________________________________
=========================PROXY CHECK/SCRAPER BY HOLLOWKAT PBHG======================
------------------------------------------------------------------------------------

			+FORMARTO PARA LOS BINS:
			+5223037787798075|05|2022|183
			-PAGINA USADA DE EJEMPLO: https://bestccgen.com/namso-ccgen/
			
"""


line = 1
while line ==1:
	print(Fore.GREEN+banner)
	print(Fore.GREEN+menu)
	print("ESCRIBA LA DIRECCION DEL ARCHIVO CON LOS BINS.")
	a = input("[PBHG]$")
	if len(str(a))  >  0:
		file().file(a)
		print("INICIANDO....")
		sleep(2)
		break
	else:
		print("ESCRIBA UNA DIRECCION VALIDA")
		goto(1)

file = open(name[0]).readlines()
file = [a.rstrip() for a in file]
line = 2
while line == 2:
	datos = [a.rstrip() for a in datos]
	for lines in datos:
		lines = lines.split("|")
		cc = lines[0]
		fecha = lines[1] 
		año = lines[2]
		driver = webdriver.Chrome()
		wait = WebDriverWait(driver, 7)
		url = """https://commerce.adobe.com/checkout/email/?items%5B0%5D%5Bid%5D=08823B2E8361CE018F9A2C51CF489283&items%5B0%5D%5Bq%5D=1&items%5B0%5D%5Bcs%5D=1&items%5B0%5D%5Bcv%5D=%5Bobject%20Object%5D&cli=creative&co=US&lang=es&oco=MX&fr=v1"""
		driver.get(url)
		a = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qe-id='user-email-input']")))
		a.send_keys("ANSDJLAHSadsasdDJAHSDJK@gmail.com")
		b = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='action-button-email']")))
		b.click()
		c = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='creditCardNumber']")))
		c.send_keys(cc)


		ad = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@data-qid='creditCardExpiryMonth']")))
		if int(fecha) > 8:
			action = ActionChains(driver)
			action.move_to_element(ad)
			action.click(ad)
			action.send_keys(Keys.ARROW_DOWN)
			action.send_keys(Keys.ARROW_DOWN)
			action.send_keys(Keys.ARROW_DOWN)
			action.send_keys(Keys.ARROW_DOWN)	
			action.send_keys(Keys.ARROW_DOWN)
			action.send_keys(Keys.ARROW_DOWN)
			action.send_keys(Keys.ARROW_DOWN)
			action.send_keys(Keys.ARROW_DOWN)
			action.send_keys(Keys.ARROW_DOWN)
			action.send_keys(Keys.ARROW_DOWN)
			action.send_keys(Keys.ENTER)

			action.perform()
		else:
			ad.click()

		k =  wait.until(EC.element_to_be_clickable((By.XPATH,f"//li[@data-value={fecha}]")))
		k.click()
		ac = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@data-qid='creditCardExpiryYear']")))
		ac.click()
		e = wait.until(EC.element_to_be_clickable((By.XPATH,f"//li[@data-value={año}]")))
		e.click()
		f = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='firstName']")))
		f.send_keys("olaytuxd")
		g = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='lastName']")))
		g.send_keys("america")
		h = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='street1']")))
		h.send_keys("4543 Street Rd")
		aa = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='postalCode']")))
		aa.send_keys("18976")
		asd = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='companyName']")))
		asd.send_keys("sd")
		bb = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@data-qe-id='action-button-payment-popup']")))	

		bb.click()
		try:

			kaka = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@data-qid='custom-error-alert-box']")))
			print("chale esta die unu")
			driver.close()
		except:
			print("live")
			
	break