import json

from custom_typing import typing_classes

from classes import message, message_types_enum
from .default_text_handler import handle_default_text
from .user_requset_handler import handle_user_request
from .incorrect_requests_handler import handle_incorrect_msg_type
from methods import send_methods, recieve_methods, disconnection_methods

writers = []

import utils

logger = utils.create_file_logger(__name__)


async def hand(reader, writer):
    writers.append(writer)
    address = utils.get_writer_address(writer)
    logger.info(f'{address} added')

    await greet_and_notify(writer, writers)

    while True:
        try:
            msg = await recieve_methods.receive_message(reader)

            logger.info(f'received {address}: {msg}')

            if not msg:
                raise ConnectionResetError

            if not ("author" in msg):
                logger.warning(f'No author for {msg}, adding')

                msg = msg[:-2] + f', "author":"{address}"' + '}'  # replacing two last symbols: } & something else
                # and adding field and author key and value
            msg = message.Message.deserialize(msg)

            if type(msg) == dict:
                logger.warning('Message type is dict, converting to standard jsonpickle str')

                msg = message.Message.create_from_dict(msg)

            if msg.msg_type == message_types_enum.MessageTypes.user_request.value:
                await handle_user_request(msg.msg, writer, writers)
            elif msg.msg_type == message_types_enum.MessageTypes.text.value:
                await handle_default_text(msg.msg, writer, writers)
            else:
                await handle_incorrect_msg_type(writer, writers, msg.msg_type)

        except (ConnectionResetError, ConnectionAbortedError):
            logger.warning(f'{address} have disconnect without saying Bye, removing')
            await disconnection_methods.close_writer_forced(writer, writers)
            break

        except json.decoder.JSONDecodeError:
            logger.exception(f'{address} sent garbage: {msg}')
            notification_for_user = message.Message(msg_type=message_types_enum.MessageTypes.text.value,
                                                    author='Server',
                                                    msg='SERVER_WARNING:Your message was garbage. If this error occurs '
                                                        'again, reinstall app OR stop using Telnet protocol')
            await send_methods.send_to_one(writer, writers, notification_for_user)


async def greet_and_notify(writer: typing_classes.StreamWriter, writers: typing_classes.Participants):
    address = utils.get_peer_name(writer)

    logger.info(f'Notifying new user about {address} joined')

    greet_msg = message.Message(msg_type=message_types_enum.MessageTypes.text.value, author='Server',
                                msg=f'Welcome to server, {address}')
    await send_methods.send_to_one(writer, writers, greet_msg)

    logger.info(f'Notifying everyone about {address} joined')

    notification_message = message.Message(msg_type=message_types_enum.MessageTypes.text.value, author='Server',
                                           msg=f'{address} joined us')
    await send_methods.forward_to_all(writer, writers, notification_message)
