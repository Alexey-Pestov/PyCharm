import vk_api

token = 'vk1.a.HSoWNtIXAgiY8GIblQdW5eobvRNkkaHRyd3DAGDI2NdJBULDB3-xmGM3hKs26C3VUdyQ4Vb_Pp3hIoDdmsFzozZ506UjTtGRN9MjqkvkglgAwPHG7dhDUk-DOV85YXFYBUI1xDtU87vBp5qRMZCU3ZltT9-C-m3V0tU9CVXmFXRGDiojFZIBdqnZgl3jIrSXRPBdclJOhzZOVdNodadzYQ'

vk = vk_api.VkApi(token=token)
vk._auth_token()

# https://vk.com/dev/messages.getConversations


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

while True:
  messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
  if messages['count']>=1:
    user_id = messages['items'][0]['last_message']['from_id']
    message_id = messages['items'][0]['last_message']['id']
    messages_text = messages['items'][0]['last_message']['text']
    if messages_text == 'курс':
      vk.method('messages.send', {'peer_id':user_id, 'random_id':message_id, 'message':rate('R01235')})
    else:
      vk.method('messages.send', {'peer_id':user_id, 'random_id':message_id, 'message':'Неизвестная команда'})
