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
    #bot.send_message(message.chat.id, welcome_text)
    keyword = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True,
                                                one_time_keyboard=False)
    # сколько кнопок в ряду, подстраиваются ли они по размеру, пропадают ли после нажатия
    button1 = telebot.types.KeyboardButton('Факт')
    button2 = telebot.types.KeyboardButton('Стих')
    button3 = telebot.types.KeyboardButton('Смешные животные')
    button4 = telebot.types.KeyboardButton('Музыка')
    keyword.add(button1,button2,button3,button4)
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyword)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = 'Муха села на варенье, Вот и всё стихотворенье'
    bot.send_message(message.from_user.id, poem_text)
    keyword = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_inline = telebot.types.InlineKeyboardButton('Перейти', url  = 'https://stihi.ru/')
    keyword.add(button_inline)
    bot.send_message(message.chat.id, 'Больше стихов', reply_markup=keyword)


@bot.message_handler(commands=['fact'])
def send_fact(message):

    responce = requests.get('https://i-fakt.ru/').content
    html = BeautifulSoup(responce, 'html.parser')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs['href']
    fact_text = fact.text
    bot.send_message(message.from_user.id, fact_text + fact_link)

@bot.message_handler(commands=['audio'])
def send_audio(message):
    song = open('Pink floyd.mp3', 'rb')
    bot.send_audio(message.chat.id, song)

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
    elif message.text.strip() == 'Факт':
        send_fact(message)
    elif message.text.strip() == 'Стих':
        send_poem(message)
    elif message.text.strip() == 'Смешные животные':
        funny(message)
    elif message.text.strip() == 'Музыка':
        send_audio(message)
    else:
        bot.send_message(message.from_user.id, 'Чё ты мне паришь?')



bot.polling(    )