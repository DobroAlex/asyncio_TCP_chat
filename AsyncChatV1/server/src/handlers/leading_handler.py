import jsonpickle
import json

from classes import message, message_types_enum
from .default_text_handler import handle_default_text
from .user_requset_handler import handle_user_request
from methods import send_methods, recieve_methods, disconnection_methods
import utils

writers = []


async def hand(reader, writer):
    writers.append(writer)
    address = utils.get_peer_name(writer)
    print(f'{address} added')

    await greet_and_notify(writer, writers)

    while True:
        try:
            msg = await recieve_methods.receive_message(reader)

            if not msg:
                raise ConnectionResetError

            msg = jsonpickle.loads(msg)

            if msg['msg_type'] == message_types_enum.MessageTypes.user_request.value:
                await handle_user_request(msg['msg'], writer, writers)
            if msg['msg_type'] == message_types_enum.MessageTypes.text.value:
                await handle_default_text(msg['msg'], writer, writers)

        except ConnectionResetError:
            print(f'{address} have disconnect without saying Bye, removing')
            await disconnection_methods.close_writer_forced(writer, writers)
            break

        except json.decoder.JSONDecodeError:
            print(f'{address} sent garbage')
            notification_for_user = message.Message(message_types_enum.MessageTypes.text.value, 'Server',
                                                    'SERVER_WARNING:Your message was garbage. If this error occurs '
                                                    'again, '
                                                    'reinstall app')
            await send_methods.send_to_one(writer, writers, notification_for_user)


async def greet_and_notify(writer, writers: list):
    address = utils.get_peer_name(writer)

    greet_msg = message.Message(message_types_enum.MessageTypes.text, 'Server', f'Welcome to server, {address}')
    await send_methods.send_to_one(writer, writers, greet_msg)

    notification_message = message.Message(message_types_enum.MessageTypes.text, 'Server', f'{address} joined us')
    await send_methods.forward_to_all(writer, writers, notification_message)
