from custom_typing import typing_classes

import methods
from classes import message, message_types_enum
import utils


async def handle_default_text(msg_text: str, writer: typing_classes.StreamWriter, writers: typing_classes.Participants):
    address = utils.get_peer_name(writer)

    msg = message.Message(msg_type=message_types_enum.MessageTypes.text.value, author=address, msg=msg_text)

    await methods.send_methods.forward_to_all(writer, writers, msg)
