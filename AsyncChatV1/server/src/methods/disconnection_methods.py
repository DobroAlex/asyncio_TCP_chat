from custom_typing import typing_classes

from classes import message, message_types_enum
from methods import send_methods
import utils

async def close_writer(writer: typing_classes.StreamWriter, writers: typing_classes.Participants):
    """
    Closes given writer and removes it from global list of writers

    :param writer: target writer which is ought to be closed
    :param writers: list of writers, usually from handlers/leading_handler.py. Writer will be excluded from
        this list (if present in one)
    :return: None
    """
    try:
        writer.close()
    except Exception as e:
        print('Some problem occurred during writer closure: ')
        address = writer.get_extra_info('peername')
        print(f'For {address}: \t {e}')
        print('But we will try to remove this writer from writers')
    finally:
        if writer in writers:
            writers.remove(writer)


async def close_writer_forced(writer: typing_classes.StreamWriter, writers: typing_classes.Participants):
    """
    Forced closure of given writer with notification about this being forwarded to every other in the chat as plaint txt

    :param writer: target writer which is ought to be closed
    :param writers: list of writers, usually from handlers/leading_handler.py. Writer will be excluded from
        this list (if present in one)
    :return:
    """
    await close_writer(writer, writers)
    address = utils.get_peer_name(writer)
    notification_for_all = message.Message(message_types_enum.MessageTypes.text.value, 'Server',
                                           f'{address} have lost connection with us')
    await send_methods.forward_to_all(writer, writers, notification_for_all)
