import requests
from bs4 import BeautifulSoup
import selenium as sl 
From selenium import webdriver

#    variaveis    #

user = ""
password = ""
navegador  = webdriver.Chrome(service=servico)
url_base = 'https://cashview.hdtdigital.com.br/CashView/Login.aspx '

filter_data = input('Qual data você deseja ? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

driver = webdriver.Chrome() 

#      login        #

navegador.find_element(By.ID,"UserName").send_keys(user)
navegador.find_element(By.ID,"Password").send_keys(password)
navegador.find_element(By.ID,"LoginButton").click()
navegador.find_element(By.ID,"LoginButton").click()










