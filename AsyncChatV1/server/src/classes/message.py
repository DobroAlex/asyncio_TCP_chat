import dataclasses

import classes.message_types_enum as message_types_enum


@dataclasses.dataclass
class Message:
    msg_type: message_types_enum.MessageTypes
    msg: str
    author: str
