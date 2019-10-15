import methods

from classes import message, message_types_enum


async def handle_default_text(msg_text, writer, writers):
    address = writer.get_extra_info('peername')

    msg = message.Message(message_types_enum.MessageTypes.text.value, address, msg_text)

    await methods.send_methods.forward_to_all(writer, writers, msg)
