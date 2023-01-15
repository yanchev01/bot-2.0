import vk_api, json
from datetime import datetime
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from samp_client.client import SampClient
import mysql.connector
import re
from bdcmd import *
from cmd import *

class MyLongPoll(VkBotLongPoll):
    def listen(self):
        while True:
            try:
                for event in self.check():
                    yield event
            except Exception as e:
                print(e)

vk_session = vk_api.VkApi(token="vk1.a.IBpFqH7-gdAjnOq_CQ4lzE_zhabjiWG7ySJfQ6rJZs1t3R90fx8r-TofEG0brwN_ingGtfoZfjDPWvHH94fJY5WhzVWsTFJ1hzM_S60W3WOHVFY4xKsSx18mdhG7eA1PXd_rZ05C9nq_Fhrkfs9Yos-7cFBYrZdVmAzHZbvqr2kNuO_ABUAFmXMdRyZWj9qz6IjI2gXgiy4t6F7dvjAClw")
longpoll = MyLongPoll(vk_session, 213308439)

def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})
def kickuser(id, user):
    vk_session.method("messages.removeChatUser", {"chat_id": id, "user_id": user, "random_id": 0})
def replace(id, text, mid):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0, 'forward': mid})

myconn = mysql.connector.connect(host="217.182.34.233", user="gs20702", password="AdvensTOP",database="gs20702")
cur = myconn.cursor()

try:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_chat:
                id = event.chat_id
                msg = event.object.message['text']
                cmd =  msg.split(' ')[0].replace('/', '')
                iduser = event.message.get('from_id')
                peer = str(int(event.chat_id) + 2000000000)
                name = vk_session.method("users.get", {"user_ids": iduser})
                peer_id = event.message.get('peer_id')
                cid = event.message.get('conversation_message_id')
                mid = json.dumps({'peer_id': peer_id, 'conversation_message_ids': cid, 'is_reply': False})
                fullname = name[0]['first_name'] + ' ' + name[0]['last_name']
                cidd(id, msg, sender)
                setadmin(id, msg, sender, cur, myconn)
                try:
                    if msg == '/online':
                        with SampClient(address='51.91.91.102', port=7777, rcon_password='sadasdadawdadawd') as client:
                            info = client.get_server_info()
                            clients = client.get_server_clients_detailed()
                            sender(id, f"Информация о сервере:\n\n{info}\n\nВерсия мода: {info.gamemode}\n\n\nОнлайн: {info.players}/{info.max_players}\nИгроки: {clients}")
                except Exception as e:
                    sender(id, f"Произошла ошибка {e}")

except:
    myconn.rollback()
myconn.close()
