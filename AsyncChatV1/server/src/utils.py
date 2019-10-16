import custom_typing.typing_classes as typing_classes


def get_peer_name(writer: typing_classes.StreamWriter) -> tuple:
    return writer.get_extra_info('peername')
