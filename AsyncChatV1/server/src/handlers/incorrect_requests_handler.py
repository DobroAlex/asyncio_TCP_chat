from custom_typing import typing_classes

from methods import send_methods
from classes import message_types_enum, message


async def handle_incorrect_msg_type(writer: typing_classes.StreamWriter, writers: typing_classes.Participants,
                                    msg_type: str):
    """
    Notifies one user that msg_type of his message is not in classes.message_types_enum.MessageTypes.
    Should / will be fired then msg_type is incorrect and the indicates that text (msg field) will NOT be proceeded

    :param writer: User which will be notified
    :param writers: all other chat participants
    :param msg_type: string representation of type which caused error. Use it for debug on client-side
    :return:
    """
    notification_for_user = message.Message(msg_type=message_types_enum.MessageTypes.text.value, author='Server',
                                            msg=f'SERVER_WARNING: Your message was of incorrect type: {msg_type} ')
    await send_methods.send_to_one(writer, writers, notification_for_user)


async def handle_incorrect_msg_text(writer: typing_classes.StreamWriter, writers: typing_classes.Participants,
                                    msg_text: str):
    """
    Notifies one user that msg (text itself) of his message can not be proceeded.
    Usually occurs not for plain text (msg_type == text) but for system information (user_request, user_respond)
    :param writer: User which will be notified
    :param writers: all other chat participants
    :param msg_text: string representation of text which caused error. Use it for debug on client-side
    :return:
    """
    notification_for_user = message.Message(msg_type=message_types_enum.MessageTypes.text, author='Server',
                                            msg=f'SERVER_WARNING: your request  {msg_text}  can not be proceeded')
    await send_methods.send_to_one(writer, writers, notification_for_user)
