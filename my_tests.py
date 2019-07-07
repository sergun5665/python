import unittest
import socket
import json


import pytest


def test_my_test():
    assert 1 == 1



class TestMyCase(unittest.TestCase):

    def test_data(self):

        valid_result = '{"msg": "Hello, my name is Andrey", "action": "do_smth"}'


        sock = socket.socket()

        sock.connect(('localhost', 7777))

        result = ""

        while True:
            data = sock.recv(1024)
            if len(data) == 0:
                break

            result = data.decode("utf-8")

        self.assertEqual(result, valid_result)

unittest.main()

