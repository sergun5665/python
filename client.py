import socket
import json
sock = socket.socket()

sock.connect(('localhost', 7777))


result = ""

while True:
    data = sock.recv(1024)
    if len(data) == 0:
        break

    result = data.decode("utf-8")

sock.close()


print(json.loads(result))


