import socket
import utils
import jim

with utils.create_tcp_client_socket("localhost", utils.PORT) as s:

    # while True:
        # msg = input("Input msg: ")

        s.send(utils.str_to_bytes(jim.get_presence_message("Andrey", "Pak")))


