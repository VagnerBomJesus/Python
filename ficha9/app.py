from flask import Flask
from selenium import webdriver
import pandas as pd
import os
import time
import smtplib
import locale
import smtplib
import ssl
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

'''p = '//*[@id=":0"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz/div/div/div/div[1]/div[2]'

locale.setlocale(locale.LC_MONETARY, 'pt_PT.UTF-8')

navegador = webdriver.Chrome()
navegador.get(
    'https://drive.google.com/drive/folders/1fBiK2RMqCiLlpQ_W4ReU0ykwWHP5yQQ6')
time.sleep(1)
navegador.find_element_by_xpath(
    '//*[@id=":0"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[1]/div/div/div/div[1]/div[2]').click()
time.sleep(15)
os.rename('C:/Users/ITCenter/Downloads/Gestão_Problemas_Mensal_EXEMPLOGRÁFICOS.xlsx',
          '')
navegador.close()
tabela = pd.read_excel(
    r"C:\\Users\\ITCenter\\python\\ficha9\\Gestão_Problemas_Mensal_EXEMPLOGRÁFICOS.xlsx")
#
display(tabela)
# time.sleep(5)

# os.remove(
#    'C:/Users/ITCenter/python/ficha9/Gestão_Problemas_Mensal_EXEMPLOGRÁFICOS.xlsx')

arq = open("tabela.html", "w")
arq.write(tabela.to_html())'''

df = pd.read_excel('C:/Users/ITCenter/python/ficha9/Gestao.xlsx')
# display(df)
ht = df.to_html()

# print(ht)


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"
