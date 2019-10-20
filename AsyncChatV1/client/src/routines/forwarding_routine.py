import jsonpickle
import json

import socket


from classes import message, message_types_enum as message_types


def forwarding_routine(main_socket: socket.socket):
    while True:
        try:
            raw_input = input()

            msg = message.Message(msg=raw_input, author='', msg_type=message_types.MessageTypes.text.value)

            msg = jsonpickle.encode(msg)
            msg = bytearray(msg, 'utf-8')

            main_socket.send(msg)

        except (ConnectionAbortedError, ConnectionResetError, ConnectionError, ConnectionRefusedError) as e:
            print('It seems that server is dead. You should try to restart the program.')
            print(f'{e}')

            break
