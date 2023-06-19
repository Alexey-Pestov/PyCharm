import random
from  course import *
from wiki import *
import  vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = 'vk1.a.HSoWNtIXAgiY8GIblQdW5eobvRNkkaHRyd3DAGDI2NdJBULDB3-xmGM3hKs26C3VUdyQ4Vb_Pp3hIoDdmsFzozZ506UjTtGRN9MjqkvkglgAwPHG7dhDUk-DOV85YXFYBUI1xDtU87vBp5qRMZCU3ZltT9-C-m3V0tU9CVXmFXRGDiojFZIBdqnZgl3jIrSXRPBdclJOhzZOVdNodadzYQ'

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        print(msg, user_id)
        random_id = random.randint(1, 1_000_000) # нужно для сервера VK
        if msg == 'курс':
            response = f'{rate("R01235")} рублей на $1, \n {rate("R01239")} рублей за €1'

        elif msg.startswith('вики'):
            article = msg[5:]
            response = get_wiki_article(article)
        else:
            response = get_wiki_article('Неизвестная команда')
        vk.messages.send(user_id=user_id, random_id=random_id, message = response[0:4096])
