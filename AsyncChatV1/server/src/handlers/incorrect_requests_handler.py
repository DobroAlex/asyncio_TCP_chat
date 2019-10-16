from custom_typing import typing_classes

from methods import send_methods
from classes import message_types_enum, message


async def handle_incorrect_msg_type(writer: typing_classes.StreamWriter, writers: typing_classes.Participants,
                                    msg_type: str):
    notification_for_user = message.Message(message_types_enum.MessageTypes.text.value, 'Server',
                                            'SERVER_WARNING: Your message was of incorrect type')
    await send_methods.send_to_one(writer, writers, notification_for_user)


async def handle_incorrect_msg_text(writer: typing_classes.StreamWriter, writers: typing_classes.Participants,
                                    msg_text: str):
    notification_for_user = message.Message(message_types_enum.MessageTypes.text, 'Server',
                                            f'SERVER_WARNING: your request  {msg_text}  can not be proceeded')
    await send_methods.send_to_one(writer, writers, notification_for_user)
