import dataclasses
import jsonpickle
import classes.message_types_enum as message_types_enum


@dataclasses.dataclass
class Message:
    msg_type: message_types_enum.MessageTypes
    msg: str
    author: str

    @staticmethod
    def deserialize(json_str: str):
        return jsonpickle.decode(json_str, classes=Message)

    @staticmethod
    def create_from_dict(target: dict):
        return Message(msg=target['msg'], author=target['author'], msg_type=target['msg_type'])