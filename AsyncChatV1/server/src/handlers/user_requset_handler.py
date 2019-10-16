from custom_typing import typing_classes

import methods
from classes import message, message_types_enum
import utils


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
    addr = utils.get_peer_name(writer)
    print(msg_text)
    if msg_text == '/exit':
        try:
            new_message = message.Message(message_types_enum.MessageTypes.text.value, addr, f'{addr} left us')
            await methods.send_methods.forward_to_all(writer, writers, new_message)

            await methods.disconnection_methods.close_writer(writer, writers)
        except Exception as e:
            print(f'{e}')

    elif msg_text == '/getusers':
        list_of_users = [utils.get_peer_name(w) for w in writers]
        new_message = message.Message(message_types_enum.MessageTypes.server_response.value, 'Server',
                                      f'{list_of_users}')

        await methods.send_methods.send_to_one(writer, writers, new_message)
    else:
        print(f'{writer}:{addr} request  {msg_text} -- cannot be proceeded')
        # TODO: add respond_to_user ('Uncrossable entity')
