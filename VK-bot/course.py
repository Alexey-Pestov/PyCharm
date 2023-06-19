import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://www.cbr.ru/scripts/XML_daily.asp?'
today = datetime.today()
today = today.strftime('%d/%m/%Y')
date = {'date_req' : today}
responce = requests.get(url, params=date)
xml = BeautifulSoup(responce.content, 'lxml')


def rate(id):
  rate = xml.find('valute', {'id' : id}).value.text
  return rate