import socket
import utils
import jim
import argparse

parser = argparse.ArgumentParser("My client parser")

parser.add_argument("host", type=str, help="Host of server")
parser.add_argument("port", type=int, help="Port of server")
parser.add_argument("mode", type=str, help="Mode of client")

args = parser.parse_args()

with utils.create_tcp_client_socket(args.host, args.port) as s:
    if args.mode == "r":
        print("Enter in read socket")
        while True:
            msg = s.recv(1024)

            print(utils.bytes_to_str(msg))
    else:
        print("Enter in write socket")

        user = input("Input user: ")
        status = input("Input status: ")
        s.send(utils.str_to_bytes(jim.get_presence_message(user, status)))
