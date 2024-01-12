import requests
from bs4 import BeautifulSoup
#import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta 

#    variaveis    #

user = ""
password = ""
servico = Service(ChromeDriverManager().install())
navegador  = webdriver.Chrome(service=servico)
url_base = 'https://cashview.hdtdigital.com.br/CashView/Login.aspx '
navegador.get(url_base)
dtainicio= datetime.now() - timedelta (1)
dtafinal= datetime.now()

#      login        #
#time.sleep (5)
navegador.find_element(By.ID,"UserName").send_keys(user)
#time.sleep (5)
navegador.find_element(By.ID,"Password").send_keys(password)
#time.sleep (5)
navegador.find_element(By.ID,"LoginButton").click()
#time.sleep (5)


#extração do arquivo#
#navegador.find_element(By.XPATH, '//*[@id="NavigationMenu"]/ul/li[3]').click()
hoverable = navegador.find_element(By.XPATH, '//*[@id="NavigationMenu"]/ul/li[3]')
ActionChains(navegador)\
        .move_to_element(hoverable)\
        .perform()
#time.sleep (2)
navegador.find_element(By.XPATH, '//*[@id="NavigationMenu:submenu:8"]/li[1]/a').click()
#time.sleep(5)
navegador.find_element(By.ID, 'MainContent_txtDataInicio').clear()
#time.sleep(2)
navegador.find_element(By.ID, 'MainContent_txtDataInicio').send_keys("dtainicio = ", dtainicio.strftime('%d-%m-%Y'))
navegador.find_element(By.XPATH, '//*[@id="MainContent_ddlHorarioInicio"]').click()
navegador.find_element(By.XPATH, '//*[@id="MainContent_ddlHorarioInicio"]/option[18]').click()
navegador.find_element(By.ID, 'MainContent_txtDataFim').send_keys("dtafinal = ", dtafinal.strftime('%d-%m-%Y'))
navegador.find_element(By.ID, 'MainContent_ddlHorarioFim').click()
navegador.find_element(By.XPATH, '//*[@id="MainContent_ddlHorarioFim"]/option[18]').click()
navegador.find_element(By.ID, 'MainContent_btnConsultar').click()
time.sleep (5)
navegador.find_element(By.XPATH, '//*[@id="ctl00_MainContent_ReportViewer1_ctl06_ctl04_ctl00"]').click()
navegador.find_element(By.XPATH, '//*[@id="ctl00_MainContent_ReportViewer1_ctl06_ctl04_ctl00_Menu"]/div[1]/a').click()


time.sleep (30)
