# ----------------------------------------------------------------------
# Message class
# ----------------------------------------------------------------------
# Copyright (C) 2022, Gufo Labs
# See LICENSE.md for details
# ----------------------------------------------------------------------

# Python modules
import dataclasses
from typing import Dict


@dataclasses.dataclass
class Message(object):
    """
    Liftbridge message.

    Args:
        value: Message body.
        subject: Message stream.
        offset: Message offset.
        timestamp: Message timestamp in UNIX format.
        key: Message key.
        partition: stream partition.
        headers: Additional message headers.
    """

    value: bytes
    subject: str
    offset: int
    timestamp: int
    key: bytes
    partition: int
    headers: Dict[str, bytes]
