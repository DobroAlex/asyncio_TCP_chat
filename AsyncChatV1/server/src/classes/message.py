import classes.message_types_enum as message_types_enum


class Message:
    def __init__(self, msg_type: message_types_enum.MessageTypes, author: str, msg: str):
        self.msg_type = msg_type
        self.msg = msg
        self.author = author
