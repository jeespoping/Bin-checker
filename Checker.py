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
PATCH = "C:\Program Files (x86)\chromedriver.exe"
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
..######..##.....##.########..######..##....##.########.########.....
.##....##.##.....##.##.......##....##.##...##..##.......##.....##....
.##.......##.....##.##.......##.......##..##...##.......##.....##....
.##.......#########.######...##.......#####....######...########.....
.##.......##.....##.##.......##.......##..##...##.......##...##......
.##....##.##.....##.##.......##....##.##...##..##.......##....##.....
..######..##.....##.########..######..##....##.########.##.....##....
"""
menu ="""

____________________________________________________________________________________
=========================PROXY CHECK/ JESUS LOPEZ FLOREZ      ======================
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
	a = "C:/Users/Jesus/Documents/checkers/Bin-checker/cc.txt"
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
contador = 1
while line == 2:
	datos = [a.rstrip() for a in datos]
	for lines in datos:
		lines = lines.split("|")
		cc = lines[0]
		fecha = lines[1] 
		año = lines[2]
		driver = webdriver.Chrome(PATCH)
		wait = WebDriverWait(driver, 7)
		url = """https://commerce.adobe.com/checkout/email?items%5B0%5D%5Bid%5D=08823B2E8361CE018F9A2C51CF489283&items%5B0%5D%5Bq%5D=1&items%5B0%5D%5Bcs%5D=1&cli=creative&co=US&lang=es&fr=v1&oco=MX"""
		driver.get(url)
		a = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qe-id='user-email-input']")))
		a.send_keys("yarobaf971@gomail4.com")
		b = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='action-button-email']")))
		b.click()
		sleep(5)
		#arroz = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
		#arroz.send_keys("nik.2000")
		#bii = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='sign_in']")))
		#bii.click()
		c = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='creditCardNumber']")))
		c.send_keys(cc)


		ad = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@data-qid='creditCardExpiryMonth']")))

		ad.click()

		k =  wait.until(EC.element_to_be_clickable((By.XPATH,f"//li[@data-value={fecha}]")))
		k.click()
		ac = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@data-qid='creditCardExpiryYear']")))
		ac.click()
		e = wait.until(EC.element_to_be_clickable((By.XPATH,f"//li[@data-value={año}]")))
		e.click()
		f = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='firstName']")))
		f.send_keys("jesus")
		g = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='lastName']")))
		g.send_keys("lopez")
		h = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='street1']")))
		h.send_keys("45 E 45th st")
		aa = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='postalCode']")))
		aa.send_keys("10080")
		asd = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-qid='companyName']")))
		asd.send_keys("sd")
		bb = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@data-qe-id='action-button-payment']")))

		bb.click()
		try:

			kaka = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@data-qid='custom-error-alert-box']")))
			print(contador,"chale esta die unu")
			sleep(2)
			driver.close()
		except:
			print("live")
			print(cc)
			print(fecha)
			print(año)
		contador = contador + 1
	break