import jsonpickle
from classes import message, message_types_enum as message_types


def forwarding_routine(main_socket):
    while True:
        raw_input = input()

        msg = message.Message(msg=raw_input, author='', msg_type=message_types.MessageTypes.text.value)

        msg = jsonpickle.encode(msg)
        msg = bytearray(msg, 'utf-8')

        main_socket.send(msg)
