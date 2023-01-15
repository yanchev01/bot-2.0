def cidd(id, msg, sender):
    if msg == '/cid':
        sender(id, f"Информация о чате:\n\nID конференции: {id}")
def getonline(id, msg, sender):
    if msg == '/online':
        with SampClient(address='51.91.91.102', port=7777, rcon_password='sadasdadawdadawd') as client:
            info = client.get_server_info()
            clients = client.get_server_clients_detailed()
            info = client.get_server_info()
            sender(id, f"{info}")
            #sender(id, f"{info.gamemoda}')
            sender(id, f'Онлайн: {info.players}/{info.max_players}')
            sender(id, f'Игроки {clients}')