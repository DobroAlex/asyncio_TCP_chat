import custom_typing.typing_classes as typing_classes


async def receive_message(reader: typing_classes.StreamReader) -> str:
    data = await reader.read(1024)
    return data.decode(errors='ignore')
