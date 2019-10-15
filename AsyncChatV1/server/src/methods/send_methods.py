import jsonpickle

import classes.message as Message


async def forward_to_all(writer, writers, msg: Message):
    for w in writers:
        if w != writer:
            await send_to_one(w, msg)


async def send_to_one(writer, msg: Message):
    try:
        final_msg = jsonpickle.dumps(msg) + '\n'
        writer.write(final_msg.encode())
    except Exception as e:
        print(f'{e}')
