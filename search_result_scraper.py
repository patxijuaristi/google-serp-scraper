# -*- coding: utf-8 -*-

import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from resultado_serp import ResultadoSerp
from utils import escribirCsv, escribirFichero

class Scraper:

    def __init__(self, ruta):
        self.rutaFicheros = ruta
        self.driver = None
    
    def initDriver(self, headless):
        try:
            chrome_options = webdriver.ChromeOptions()
            if(headless):
                chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--log-level=3')
            s=Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=s, options=chrome_options)
            self.driver.get('https://www.google.com/')            
            self.driver.find_element(By.XPATH,'//*[@id="L2AGLb"]').click()
            return True
        except:
            print('Error with the Chrome Driver')
            return False
    
    def establecerAjustes(self, captcha):
        resultadosPorPag = 30
        if(captcha):
            resultadosPorPag = 100
        try:
            url = 'https://www.google.com/preferences'
            self.driver.get(url)
            time.sleep(random.randint(1,3))
            
            inputValue = self.driver.find_element(By.XPATH,'//*[@id="srhSec"]/div[2]/input')            
            self.driver.execute_script("arguments[0].setAttribute('value', "+str(resultadosPorPag)+")", inputValue)

            botonGuardar = self.driver.find_element(By.XPATH,'//*[@id="form-buttons"]/div[1]')
            botonGuardar.click()
            
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()

            if(captcha):
                WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

            wait = WebDriverWait(self.driver, 100)
            wait.until(EC.title_is('Google'))

            return True
        except Exception as e:
            print(e)
            print('Some error occurred qith the settings')
            return False
    
    def scrapear(self, kw, captcha, maxPaginas):
        if(self.establecerAjustes(captcha) == False):
            return False
        listaResultados = []
        numPagina = 1
        try:
            url = 'https://www.google.com/search?q='+kw.replace(' ','+')+'&filter=0'
            self.driver.get(url)

            while(numPagina < maxPaginas):

                serp = self.driver.find_elements(By.CSS_SELECTOR,'.tF2Cxc')

                for resultado in serp:
                    titulo = resultado.find_element(By.TAG_NAME, 'h3')
                    enlace = resultado.find_element(By.CSS_SELECTOR, '.yuRUbf a')
                    descripcion = resultado.find_element(By.CSS_SELECTOR, '.IsZvec')

                    resultSerp = ResultadoSerp()
                    resultSerp.titulo = titulo.text
                    resultSerp.enlace = enlace.get_attribute('href')
                    resultSerp.metadescripcion = descripcion.text.replace('\n','. ')

                    if(resultSerp.enlace != '' or resultSerp.enlace != None):
                        listaResultados.append(resultSerp)
                
                WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pnnext"]'))).click()
                time.sleep(2)
                numPagina += 1
            
            raise TimeoutException('Llegado a la página ' + str(numPagina))

        except (NoSuchElementException, TimeoutException):
            print('No hay más páginas. Proceso FInalizado')
            escribirCsv('.', kw, listaResultados)
            escribirFichero('.', kw, listaResultados)
            print('Fichero escrito')
        except Exception:
            print('Some error occurred')
            return False
    
    def endDriver(self):
        self.driver.quit()