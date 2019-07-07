import socket
import json
import random

sock = socket.socket()

sock.bind(('', 7777))

sock.listen(1)

data = {
    "msg": "Hello, my name is Sergey",
    "action": "do_smth"
}

data2 = {
    "msg": "Hello, my name is Sergey",
    "action": "do_smth2"
}

s_data = json.dumps(data)
s_data2 = json.dumps(data2)


while True:
    client, addr = sock.accept()
    print(f"Получен запрос на соединение от {str(addr)}")

    if random.choice([0,12,3,4,5,6,7,8,8,9]) == 0:
        client.send(s_data.encode("utf-8"))
    else:
        client.send(s_data2.encode("utf-8"))


    client.close()
