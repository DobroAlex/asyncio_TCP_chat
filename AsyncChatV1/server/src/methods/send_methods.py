import jsonpickle

import classes.message as message
from .disconnection_methods import close_writer_forced


async def forward_to_all(writer, writers, msg: message):
    for w in writers:
        if w != writer:
            await send_to_one(w, writers, msg)


async def send_to_one(writer, writers: list, msg: message):
    """
    Sends given msg to writer. Adds new line at the end of the message. If there is an error,
    writer will be forced to close
    :param writer:
    :param msg: Message
    :return:
    """
    try:
        final_msg = jsonpickle.dumps(msg) + '\n'  # Some telnet clients such as netcat/ncat or PuTTy dosen't
        # automatically print \n at the end of message
        writer.write(final_msg.encode())
    except Exception as e:
        print(f'{e}')
        close_writer_forced(writer, writers)
