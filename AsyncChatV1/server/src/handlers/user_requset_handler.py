# from main import logger


import methods
from classes import message, message_types_enum


# import logging

async def handle_user_request(msg_text, writer, writers):
    addr = writer.get_extra_info('peername')
    print(msg_text)
    if msg_text == '/exit':
        try:
            # logger.info(f'{writer}:{addr} removed')
            new_message = message.Message(message_types_enum.MessageTypes.text.value, addr, f'{addr} left us')
            await methods.send_methods.forward_to_all(writer, writers, new_message)

            writer.close()
            writers.remove(writer)
        except Exception as e:
            print(f'{e}')
            pass

    elif msg_text == '/getusers':
        list_of_users = [w.get_extra_info('peername') for w in writers]
        new_message = message.Message(message_types_enum.MessageTypes.server_response.value, 'Server', f'{list_of_users}')

        await methods.send_methods.send_to_one(writer, new_message)
    else:
        print(f'{writer}:{addr} request  {msg_text} -- cannot be proceeded')
        # TODO: add respond_to_user ('Uncrossable entity')
