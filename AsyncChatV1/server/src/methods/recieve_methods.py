async def receive_message(reader) -> str:
    data = await reader.read(1024)
    return data.decode(errors='ignore')
