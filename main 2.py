import vk_api
import sqlite3
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import datetime
import re

cmds = ['kick', 'кик']

vk_session = vk_api.VkApi(token = "bd0bad70d5169d9d298b705ca5e159f1a4d34dc272287969dc8da141892d84d517d06d0ab084e5c5f68ed")
longpoll = VkBotLongPoll(vk_session, 213308439)
db = sqlite3.connect('action.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (
    userId BIGINT,
    act TEXT,
    fio TEXT,
    gender TEXT,
    age TEXT
)""")
db.commit()

userAct = '0'
    

def sender(id, text):
    vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})


def kikuser(id, user):
    vk_session.method("messages.removeChatUser", {"chat_id": id, "user_id": user, "random_id": 0})

def fixMsg(msg):
    msg = "'"+msg+"'"
    return msg

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:


            id = event.chat_id
            msg = event.object.message['text']
            cmd = msg.split(' ')[0].replace('/', '')
            iduser = event.message.get('from_id')


            if cmd in cmds and '[' in msg and ']' in msg:
                try:
                    idd = re.findall(rf'/{cmd} \[id(\d*)\|.*]', msg)[0]
                    kick_type = 'С возможностью возвращения'
                    try:
                        msg1 = msg.split(' ')[2]
                        kikuser(id, idd)
                        sender(id, f"@id{idd}(Пользователь) успешно исключён из беседы.\nАдминистратор: @id{iduser}(Администратор)\n"
                                   f"Дата:  {datetime.datetime.now().strftime(' %d.%m.%Y')}\nВремя:{datetime.datetime.now().strftime(' %H:%M:%S')}\n"
                                   f"Причина: {msg1}\nТип кика: {kick_type}")
                        print(iduser, 'use command kick', idd)
                    except:
                        kikuser(id, idd)
                        sender(id,
                               f"@id{idd}(Пользователь) успешно исключён из беседы.\nАдминистратор: @id{iduser}(Администратор)\n"
                               f"Дата:  {datetime.datetime.now().strftime(' %d.%m.%Y')}\nВремя:{datetime.datetime.now().strftime(' %H:%M:%S')}\n"
                               f"Причина: Нет причины\nТип кика: {kick_type}")
                            print(iduser, 'use command kick', idd)
                except Exception as e:
                    sender(id, f'@id{iduser}(Администратор), за это тебя могут снять!\n\nВозможные причины появления данного сообщения:'
                               f'\n1. Вы попытались кикнуть человека старше Вас рангом.\n'
                               f'2. Вы не указали причину для кика\n'
                               f'3. Вы гей')
                    print('Администратор с id',iduser, ' Попытка кикнуть одного из членов whitelist')

            if msg in ['/kick', '/кик']:
                sender(id, 'Ошибка при использовании команды!\nИспользуйте /kick пользователь причина \n\nУчтите, что все Ваши действия логгируются!\n\nВ случае, если причина не будет указана Вас могут снять с поста!')
