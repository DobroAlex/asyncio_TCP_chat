from typing import *
import asyncio

import classes.message as message
import classes.message_types_enum as message_types_enum

StreamWriter = asyncio.streams.StreamWriter
StreamReader = asyncio.streams.StreamReader

Participants = List[StreamWriter]

Message = message.Message
MessageTypes = message_types_enum.MessageTypes
