import custom_typing.typing_classes as typing_classes


def get_peer_name(writer: typing_classes.StreamWriter) -> tuple:
    """
    Returns IP and port of writer
    :param writer: StreamWriter which IP and port will be returned
    :return: ("IP", port)
    """
    return writer.get_extra_info('peername')


def get_writer_address(writer: typing_classes.StreamWriter) -> tuple:
    """
    Wrapper for get_peer_name()
    :param writer: Writer which IP and port will be returned
    :return: ("IP", port)
    """
    return get_peer_name(writer)
