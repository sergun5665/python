import socket
import utils

with utils.create_tcp_client_socket("localhost", utils.PORT) as s:
    while True:
        msg = s.recv(1024)

        print(utils.bytes_to_str(msg))


