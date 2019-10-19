import custom_typing.typing_classes as typing_classes


async def receive_message(reader: typing_classes.StreamReader) -> str:
    """Reads and decodes 1024 bytes (should de enough for chat unless you're sending entire Wiki article.

        :param reader: a reader object that provides APIs to read data from the IO stream.

        :return: Decoded data string (it's expected to be either JSON serialized object or empty string
    """
    data = await reader.read(1024)
    return data.decode(errors='ignore')
