import socket
import log_config

PORT = 6666
ENCODING = 'utf-8'


def create_tcp_server_socket(address, port, listen_count):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((address, port))
    s.listen(listen_count)
    s.settimeout(0.2)

    return s


def create_tcp_client_socket(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((address, port))

    return s


def str_to_bytes(msg):
    return msg.encode(ENCODING)


def bytes_to_str(msg):
    return msg.decode(ENCODING)


def log(msg):
    def log_add(func):
        def wrapper(*args, **kwargs):
            log_config.logger.info(f"{msg} - Args: {args}, Kwargs: {kwargs}")
            return func(*args, **kwargs)
        return wrapper
    return log_add
