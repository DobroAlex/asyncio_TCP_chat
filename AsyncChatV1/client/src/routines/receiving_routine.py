import socket
import jsonpickle

from classes import message, message_types_enum as message_types


def receiving_routine(main_socket: socket.socket):
    while True:
        msg = main_socket.recv(1024)

        msg = msg.decode('utf-8', errors='ignore')
        msg = msg.replace('\n', ' ').replace('\r', ' ')

        msg = jsonpickle.decode(msg)

        if type(msg) == dict:
            msg = message.Message.create_from_dict(msg)

        if msg.msg_type == message_types.MessageTypes.text.value:
            print(f'{msg.author}: {msg.msg}')
