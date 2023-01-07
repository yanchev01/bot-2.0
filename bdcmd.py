def setadmin(id, msg, sender, cur, myconn):
    try:
        if msg.startswith('/setadmin'):
            msg5 = msg.split(' ')[1]
            msg6 = msg.split(' ')[2]
            cur.execute(f"SELECT * from accounts WHERE name = '{msg5}'")
            rowsss = cur.fetchall()
            if cur.rowcount > 0:
                if f"{msg6}" >= '1' and f"{msg6}" < '8':
                    cur.execute(f"UPDATE accounts set admin = {msg6} where name = '{msg5}'")
                    myconn.commit()
                    sender(id, f"{msg5} назначен на пост администратора {msg6} уровня")
                if f"{msg6}" == '0':
                    cur.execute(f"UPDATE accounts set admin = '0' where name = '{msg5}'")
                    myconn.commit()
                    sender(id, f'{msg5} снят с поста администратора')
                if f"{msg6}" < '0' or f"{msg6}" >= '8':
                    sender(id, 'От 1 до 7')
            else:
                sender(id, 'Данный пользователь не найден')
    except Exception as e:
        sender(id, 'Используйте: /setadmin Nick лвл')
        print(e)