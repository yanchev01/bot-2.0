def cidd(id, msg, sender):
    if msg == '/cid':
        sender(id, f"Информация о чате:\n\nID конференции: {id}")