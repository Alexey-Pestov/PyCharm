import telebot

token = '6694216605:AAGxT7wOR6Coec-RzbHMSZqpCek-CRfg7uA'
# бот alex_pestov_bot

bot = telebot.TeleBot(token)

# @bot.message_handler(content_types=['text']) # отправляем пользователю его же сообщение
# def repeat_all_messages(message):
#     bot.send_message(message.chat.id, message.text)
#     print(message)

ansr = None
x = 0
check = ''

@bot.message_handler(commands=['reset'])
def controls(message):
    global x
    global check
    global score
    global answer

    ansr = None
    x = 0
    check = ''
    bot.send_message(message.chat.id, 'Отправь 1, чтобы начать')

@bot.message_handler(content_types=['text'])
def game(message):
    global x
    global check
    global score

    ansr = str.upper(message.text)
    if (ansr == 'A' or ansr == 'B' or ansr == 'C' or ansr == 'D') and x < 14:
        if ansr == correctAnswer[x]:
            bot.send_message(message.chat.id, 'Правильно!')
            x += 1
            bot.send_message(message.chat.id, f'Текущий счет: {valueWon[x]}')
            bot.send_message(message.chat.id, question[x] + '\n' + multi1[x]+ '\n' + multi2[x] + '\n' + multi3[x]+ '\n' + multi4[x])
        else:
            bot.send_message(message.chat.id, 'Неправильно! Игра начинается заново!')
            bot.send_message(message.chat.id, 'Финальный счет: ' + valueWon[x])
            x = 0
            bot.send_message(message.chat.id, 'Отправь 1, чтобы начать')
    elif (ansr == 'A' or ansr == 'B' or ansr == 'C' or ansr == 'D') and x == 14:
        if ansr == correctAnswer[x]:
            bot.send_message(message.chat.id, 'Победа!')
            bot.send_message(message.chat.id, f'Финальный счет: {valueWon[x]}')
        else:
            bot.send_message(message.chat.id, 'Прости, но ты ошибся на самом последнем вопросе и потерял все деньги. Но ты всегда можешь попробовать еще раз.')
            x = 0
    else:
        bot.send_message(message.chat.id, question[x] + '\n' + multi1[x]+ '\n' + multi2[x] + '\n' + multi3[x]+ '\n' + multi4[x])

# ниже приводится список вопросов и ответов
question = ['1 - Что совершил герой греческой мифологии Геракл?', '2 - Как зовут протагониста в Minecraft?',
            '3 - Какого специалиста следует вызвать, если у вас на кухне течёт кран?',
            '4 - Лист какого дерева украшает канадский флаг?',
            '5 - На какую сторону света показывает синий конец стрелки компаса в лесу?',
            '6 - Как назывался космический корабль Юрия Гагарина?', '7 - Что умеют делать мадагаскарские тараканы?',
            '8 - Какая из этих знаменитых башен самая низкая?', '9 - В честь кого Июль так называется?',
            '10 - Что изобрел Жак Ив Кусто?', '11 - Чем бьют по шару игроки в крокет?',
            '12 - Какой канал делит одну из частей света почти пополам и соединяет два океана?',
            '13 - Кто из этих животных откладывает яйца?',
            '14 - Что представляет собой нимб, если перевести это слово с латыни?',
            '15 - Одним из направлений какой религиозной философии является учение дзен?']
multi1 = ['A: 12 подвигов', 'A: Мстислав ', 'A: теплотехник ', 'A: берёза ', 'A: юг ', 'A: «Восход» ', 'A: пищать ',
          'A: Спасская ', 'A: Пифагор ', 'A: батискаф ', 'A: битой ', 'A: Панамский канал ', 'A: опоссум ',
          'A: облако ', 'A: Буддизм ']
multi2 = ['B: 12 деяний', 'B: Стив ', 'B: зоотехник ', 'B: осина ', 'B: запад ', 'B: «Восток» ', 'B: шипеть ',
          'B: Пизанская ', 'B: Аристотель', 'B: ласты ', 'B: клюшкой', 'B: Суэцкий канал ', 'B: утконос ', 'B: сияние ',
          'B: Иудаизм']
multi3 = ['C: 12 поступков', 'C: Шепард ', 'C: сантехник ', 'C: клён', 'C: восток', 'C: «Союз» ', 'C: кашлять ',
          'C: Эйфелева ', 'C: Юлий Цезарь ', 'C: акваланг ', 'C: молотком ', 'C: Кильский канал ', 'C: выхухоль ',
          'C: круг ', 'C: Индуизм']
multi4 = ['D: 12 побегов', 'D: Тэрри ', 'D: пиротехник ', 'D: бук ', 'D: север ', 'D: «Буран» ', 'D: ругаться ',
          'D: Останкинская ', 'D: Цицерон ', 'D: подводную кинокамеру ', 'D: лопаткой ', 'D: Волго-Донской канал ',
          'D: летучая мышь ', 'D: свет', 'D: Даосизм']
correctAnswer = ['A', 'B', 'C', 'C', 'D', 'B', 'B', 'B', 'C', 'C', 'C', 'A', 'B', 'A', 'A']
valueWon = ['0', '100', '200', '300', '500', '1,000', '1,500', '3,000', '5,000', '7,500', '15,000', '25,000', '50,000',
            '100,000', '250,000', '1,000,000']



bot.polling(none_stop=True, interval=0) # зацикливаем работу бота
