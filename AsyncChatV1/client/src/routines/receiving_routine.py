import socket
import jsonpickle
import json

from classes import message, message_types_enum as message_types


def receiving_routine(main_socket: socket.socket):
    while True:
        try:
            msg = main_socket.recv(1024)

            msg = msg.decode('utf-8', errors='ignore')
            msg = msg.replace('\n', ' ').replace('\r', ' ')

            msg = jsonpickle.decode(msg)

            if type(msg) == dict:
                msg = message.Message.create_from_dict(msg)

            if msg.msg_type == message_types.MessageTypes.text.value:
                print(f'{msg.author}: {msg.msg}')

        except json.JSONDecodeError:  # This should NOT occur normally
            print(f'SYS_WARNING: Wow, server is sending garbage. That\'s unusual: f{msg}')

        except (ConnectionAbortedError, ConnectionResetError, ConnectionError, ConnectionRefusedError) as e:
            print('It seems that server is dead. You should try to restart the program.')
            print(f'{e}')

            break

