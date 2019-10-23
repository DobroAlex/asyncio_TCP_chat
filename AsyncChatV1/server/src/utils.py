import sys
import logging

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


def create_file_logger(file_name: str, stream=sys.stdout, level=logging.INFO) -> logging.Logger:
    """
    Creates specific logger for given file. It's expected that this function will be called once per each file
    :param file_name: best way to get one -- use __name__
    :param stream: output stream for logging. Normal stdout by default
    :param level: default logging level
    :return: new logging object
    """
    # https://stackoverflow.com/questions/15727420/using-python-logging-in-multiple-modules
    logging.basicConfig(stream=stream, level=level)
    file_name_stripped = file_name.replace('__', ' ')
    return logging.getLogger(file_name_stripped)
