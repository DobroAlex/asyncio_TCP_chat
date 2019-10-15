import enum


class MessageTypes(enum.Enum):
    text = 'text'  # Plain message from user to other users
    user_request = 'user_request'  # Request from user to server such as /stop, /getusers, etc
    server_request = 'server_request'  # Request from server to user, mostly /is_alive
    user_response = 'user_response'  # Response from user to server after server_request
    server_response = 'server_response'  # Response from server to user after user_request
