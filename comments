#try:
                #    if msg == '/atm':
                #        idd = ''
                #        cur.execute("SELECT * from atm")
                #        rows = cur.fetchall()
                #        for row in rows:
                #            idd += f"{row[0]} — {row[1]},{row[2]},{row[3]}\n"
                #        sender(id, f"ID corX corY corZ \n\n{idd}")
                #except Exception as e:
                #    sender(id, f'Произошла ошибка при получении информации')

                #try:
                #    if msg.startswith('/addatm'):
                #        msg1 = msg.split(' ')[1]
                #        msg2 = msg.split(' ')[2]
                #        msg3 = msg.split(' ')[3]
                #        cur.execute(f"INSERT INTO atm (aX, aY, aZ, arX, arY, arZ) VALUES ('{msg1}', '{msg2}', {msg3}, '0', '0', '0')")
                #        myconn.commit()
                #        sender(id, f"Банкомат успешно создан")
                #except Exception as e:
                #    sender(id, f"Используйте: /addatm X Y Z")

                #try:
                #    if msg.startswith('/removeatm'):
                #        msg4 = msg.split(' ')[1]
                #        cur.execute(f"SELECT * from atm WHERE id = '{msg4}' ")
                #        rowss = cur.fetchall()
                #        if cur.rowcount > 0:
                #            cur.execute(f"DELETE from atm WHERE id = '{msg4}'")
                #            myconn.commit()
                #            sender(id, f'Банкомат с ID {msg4} успешно удалён')
                #        else:
                #            sender(id, 'Банкомата с данным ID не существует на сервере')
                #except Exception as e:
                #    sender(id, f"Используйте: /removeatm ID банкомата")