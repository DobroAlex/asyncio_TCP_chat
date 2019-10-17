import jsonpickle
import json

from custom_typing import typing_classes

from classes import message, message_types_enum
from .default_text_handler import handle_default_text
from .user_requset_handler import handle_user_request
from .incorrect_requests_handler import handle_incorrect_msg_type
from methods import send_methods, recieve_methods, disconnection_methods
import utils

writers = []


async def hand(reader, writer):
    writers.append(writer)
    address = utils.get_writer_address(writer)
    print(f'{address} added')

    await greet_and_notify(writer, writers)

    while True:
        try:
            msg = await recieve_methods.receive_message(reader)

            if not msg:
                raise ConnectionResetError

            msg = jsonpickle.decode(msg)

            if msg['msg_type'] == message_types_enum.MessageTypes.user_request.value:
                await handle_user_request(msg['msg'], writer, writers)
            elif msg['msg_type'] == message_types_enum.MessageTypes.text.value:
                await handle_default_text(msg['msg'], writer, writers)
            else:
                handle_incorrect_msg_type(writer, writers, msg['msg_type'])
        except (ConnectionResetError, ConnectionAbortedError):
            print(f'{address} have disconnect without saying Bye, removing')
            await disconnection_methods.close_writer_forced(writer, writers)
            break

        except json.decoder.JSONDecodeError:
            print(f'{address} sent garbage')
            notification_for_user = message.Message(msg_type=message_types_enum.MessageTypes.text.value,
                                                    author='Server',
                                                    msg='SERVER_WARNING:Your message was garbage. If this error occurs '
                                                    'again, '
                                                    'reinstall app')
            await send_methods.send_to_one(writer, writers, notification_for_user)


async def greet_and_notify(writer: typing_classes.StreamWriter, writers: typing_classes.Participants):
    address = utils.get_peer_name(writer)

    greet_msg = message.Message(msg_type=message_types_enum.MessageTypes.text, author='Server',
                                msg=f'Welcome to server, {address}')
    await send_methods.send_to_one(writer, writers, greet_msg)

    notification_message = message.Message(msg_type=message_types_enum.MessageTypes.text, author='Server',
                                           msg=f'{address} joined us')
    await send_methods.forward_to_all(writer, writers, notification_message)
