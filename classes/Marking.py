from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from random import randint
import logging
import logging.handlers
import os.path
import sys
from pyvirtualdisplay import Display
from datetime import datetime


class Marking(object):

	def __init__(self, user, password, dirname, markType, driverPath):
		self.user = user
		self.password = password
		self.dirname = dirname
		self.markType = markType
		self.driverPath = driverPath
		#self.display = Display(visible=0, size=(900, 700))

	def mark(self):
		#self.display.start()
		self.browser = webdriver.Chrome(self.driverPath)
		self.Log = self.log(self.dirname)
		self.Log.info(self.user+"-> Iniciando")
		self.attempLogin()

	def log(self,dirname):
	    # Archivo de log
		output_dir = dirname+"/log"
		fileName = '{:%Y-%m-%d}.log'.format(datetime.now())
		handler = logging.handlers.WatchedFileHandler(
			os.path.join(output_dir, fileName)
		)
		logger = logging.getLogger(fileName)
		pid     = os.getpid()
		handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s ["+str(pid)+"] %(message)s"))
		logger.addHandler(handler)
		logger.setLevel(logging.INFO)
		return logger

	#trae pagina login
	def attempLogin(self):
		self.browser.get('https://trabajador.relojcontrol.com')
		time.sleep(2)
		if(self.browser.title == "502 Bad Gateway" or self.browser.title == "504 Gateway Time-out" ):
			self.attempLogin()
		else:
			self.doLogin()

	def doLogin(self):

		loginButton = self.browser.find_element_by_xpath(
			"//div[@id='empleado_tab']/div[1]/div[2]/a[1]"
		)

		username = self.browser.find_element_by_xpath(
			"//div[@id='empleado_tab']/div[1]/div[1]/div[6]/input[1]"
		)
		username.send_keys(self.user)

		password = self.browser.find_element_by_xpath(
			"//div[@id='empleado_tab']/div[1]/div[1]/div[9]/input[1]"
		)
		password.send_keys(self.password)
		time.sleep(1)
		loginButton.click()
		self.browser.implicitly_wait(5)
		
		#seleccion de empresa
		company = self.browser.find_element_by_xpath(
			"//form[1]/div[1]/div[2]/div[1]/div[1]/div[3]/table[1]/tbody[1]/tr[1]"
		)
		company.click()
		time.sleep(1)
		
		buttonCompany = self.browser.find_element_by_xpath(
			"//div[@class='modal-footer z-div']/button[1]"
		)
		buttonCompany.click()
		self.Log.info(self.user+"-> Login success")

		self.doMark()
	
	def doMark(self):
		time.sleep(5)
		text = "Registrar entrada" if self.markType == 'IN' else "Registrar salida" 
		
		try:
			buttonMark = self.browser.find_element_by_xpath(
				'//button[text()="'+text+'"]'
			)
			buttonMark.click()

			confirmButton = self.browser.find_element_by_xpath(
				'//button[text()="Registrar"]'
			)
			confirmButton.click()
		except NoSuchElementException:
			self.Log.info(self.user+"-> No encuentro botones macado "+self.markType)
			self.doMark()
			
		self.Log.info(self.user+"-> Marcado "+self.markType)
		self.validate()

	def validate(self):
		self.Log.info(self.user+"-> Validando "+self.markType)
		time.sleep(2)
		try:
			buttonOk = self.browser.find_element_by_xpath(
				"//div[@class='z-window z-window-noborder z-window-noheader z-window-modal z-window-shadow']"
				+"/div[1]/div[1]/div[2]/button[1]"
			)
			buttonOk.click()
		except NoSuchElementException:
			self.Log.info(self.user+"-> No Marco "+self.markType)
			self.doMark()

		self.Log.info(self.user+"-> Finalizo"+self.markType)
		self.browser.quit() 