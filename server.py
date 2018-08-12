import socket
import select
import utils
import json

RESPONSE_OK = 200
RESPONSE_ERROR = 400


@utils.log("Reading messages")
def read_messages(r, clients):
    messages = []

    for sock in r:
        try:
            message = utils.bytes_to_str(sock.recv(1024))
            messages.append(message)
        except:
            clients.remove(sock)

    return messages


@utils.log("Sending messages")
def send_messages(messages, w, clients):
    for sock in w:
        for message in messages:
            try:
                sock.send(utils.str_to_bytes(message))
            except:
                sock.close()
                clients.remove(sock)


@utils.log("Parse presence message")
def parse_presence_message(msg_dict):
    result = RESPONSE_OK

    fields = ['action', 'time', 'user']

    if not all([field in msg_dict for field in fields]):
        result = RESPONSE_ERROR

    return json.dumps({"response": result})


@utils.log("Convert messages from str to dictionary")
def convert_messages_to_dict(messages):
    return [json.loads(i) for i in messages]


@utils.log("Parse all presence messages")
def parse_all_messages(dict_messages):
    result = []

    for msg in dict_messages:
        result.append(parse_presence_message(msg))

    return result


@utils.log("Start server mainloop")
def mainloop():
    with utils.create_tcp_server_socket('', utils.PORT, 15) as s:
        clients = []
        while True:

            try:
                client, address = s.accept()

            except OSError:
                pass
            else:
                print(f"Клиент подключился {address}")
                clients.append(client)
            finally:

                r = []
                w = []
                try:
                    r, w, e = select.select(clients, clients, [], 0)
                except:
                    pass

                if len(clients) > 0:
                    messages = read_messages(r, clients)

                    if len(messages) > 0:
                        dict_messages = convert_messages_to_dict(messages)
                        answers = parse_all_messages(dict_messages)

                        send_messages(answers, w, clients)


mainloop()


