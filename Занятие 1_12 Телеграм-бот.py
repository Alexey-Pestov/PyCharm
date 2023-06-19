import telebot
import random
import requests
from bs4 import BeautifulSoup
import re

token = '5718094547:AAEEJwo91BVR11sVnXIETmPsOtS-211P7ZQ'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    #print(message)
    welcome_text = '''
    Привет! Я очень умный!
    Вот что я умею.
    '''
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = 'Муха села на варенье, Вот и всё стихотворенье'
    bot.send_message(message.from_user.id, poem_text)

@bot.message_handler(commands=['fact'])
def send_fact(message):

    responce = requests.get('https://i-fakt.ru/').content
    html = BeautifulSoup(responce, 'html.parser')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs['href']
    fact_text = fact.text
    bot.send_message(message.from_user.id, fact_text + fact_link)

@bot.message_handler(commands=['funny'])
def funny(message):

  responce = requests.get('https://bipbap.ru/jivotnie/samye-krasivye-i-milye-zhivotnye-100-foto.html', headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
  responce = responce.content
  html = BeautifulSoup(responce, 'lxml')
  subtitle = html.find_all(src = re.compile('zhivotnie-zhivotnie-krasivo-foto'))

  A = []
  for element in subtitle:
    A.append(element['src'])

  image = A[random.randint(0, len(A)-1)]
  img_data = requests.get(image).content
  with open('funny_animal.jpg', 'wb') as handler:
      handler.write(img_data)

  funny_img = open('funny_animal.jpg', 'rb')
  bot.send_photo(message.chat.id, funny_img)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    hi = ['Привет!','Здорово!','Салют!','И тебе не хворать!','Хай!','Категорически приветствую!']
    hi_ = random.choice(hi)
    if message.text == 'привет':
        bot.send_message(message.from_user.id, hi_)
    elif message.text == 'как дела?':
        bot.send_message(message.from_user.id, 'Что-то с утра хреново...')
    else:
        bot.send_message(message.from_user.id, 'Чё ты мне паришь?')



bot.polling(    )