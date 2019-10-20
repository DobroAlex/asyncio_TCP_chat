import dataclasses
import enum


@dataclasses.dataclass
class MessageTypes(enum.Enum):
    text: str = 'text'  # Plain message from user to other users
    user_request: str = 'user_request'  # Request from user to server such as /stop, /getusers, etc
    server_request: str = 'server_request'  # Request from server to user, mostly /is_alive
    user_response: str = 'user_response'  # Response from user to server after server_request
    server_response: str = 'server_response'  # Response from server to user after user_request
