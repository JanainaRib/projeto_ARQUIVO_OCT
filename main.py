import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#    variaveis    #

user = "br05731472"
password = "janaina"
servico = Service(ChromeDriverManager().install())
navegador  = webdriver.Chrome(service=servico)
url_base = 'https://cashview.hdtdigital.com.br/CashView/Login.aspx '
navegador.get(url_base)

#      login        #
time.sleep (5)
navegador.find_element(By.ID,"UserName").send_keys(user)
time.sleep (5)
navegador.find_element(By.ID,"Password").send_keys(password)
time.sleep (5)
navegador.find_element(By.ID,"LoginButton").click()
time.sleep (5)









