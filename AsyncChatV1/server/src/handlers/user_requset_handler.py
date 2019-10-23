from custom_typing import typing_classes

import methods
from classes import message, message_types_enum
from .incorrect_requests_handler import handle_incorrect_msg_text
import utils

logger = utils.create_file_logger(__name__)


async def handle_user_request(msg_text: str, writer: typing_classes.StreamWriter, writers: typing_classes.Participants):
    """
    Handles user request. The user request as object should contain field "msg_type" : "user_request", and text should
    starts with / like "msg": "/some_command". If given command is not in the list the user will receive special plain
    text message about this

    :param msg_text: command to be proceeded. Is ought to be extracted from message by upper level handler
    :param writer: message author
    :param writers: list of all users in chat
    :return:
    """
    address = utils.get_writer_address(writer)

    if msg_text == '/exit':
        try:
            new_message = message.Message(msg_type=message_types_enum.MessageTypes.text.value, author=address,
                                          msg=f'{address} left us')

            logger.info(f'Notifying everyone that {utils.get_writer_address(writer)} leaving')

            await methods.send_methods.forward_to_all(writer, writers, new_message)

            await methods.disconnection_methods.close_writer(writer, writers)

            logger.info(f'Connection with {utils.get_writer_address(writer)} left us')

        except Exception as e:
            logger.exception(f'{e}') # this shouldn't normally occur

    elif msg_text == '/getusers':
        list_of_users = [utils.get_peer_name(w) for w in writers]
        new_message = message.Message(msg_type=message_types_enum.MessageTypes.server_response.value, author='Server',
                                      msg=f'{list_of_users}')

        logger.info(f'Sending list of users to {utils.get_writer_address(writer)}')

        await methods.send_methods.send_to_one(writer, writers, new_message)
    else:
        logger.warning(f'{address} request is {msg_text} -- cannot be proceeded')
        await handle_incorrect_msg_text(writer, writers, msg_text)
