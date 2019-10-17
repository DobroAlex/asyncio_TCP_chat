import jsonpickle

from custom_typing import typing_classes

from .disconnection_methods import close_writer_forced


async def forward_to_all(writer: typing_classes.StreamWriter, writers: typing_classes.Participants,
                         msg: typing_classes.Message):
    """
    Sends given message to everyone in list of writers except for writer who is assumed to be an author and thus
    already have this message

    :param writer:
    :param writers:
    :param msg:
    :return:
    """
    for w in writers:
        if w != writer:
            await send_to_one(w, writers, msg)


async def send_to_one(writer: typing_classes.StreamWriter, writers: typing_classes.Participants, msg: typing_classes.Message):
    """
    Sends given msg to writer. Adds new line at the end of the message. If there is an error,
    writer will be forced to close

    :param writer: messenger recipient
    :param msg: a message to be delivered
    :return:
    """
    try:
        final_msg = jsonpickle.encode(msg) + '\n'  # Some telnet clients such as netcat/ncat or PuTTy dosen't
        # automatically print \n at the end of message
        writer.write(final_msg.encode())
    except Exception as e:
        print(f'{e}')
        close_writer_forced(writer, writers)
