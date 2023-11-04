from abc import ABC, abstractmethod
from typing import Any
from dataclasses import dataclass


class Packet(ABC):
    def __init__(self, data: dict[str, Any]):
        self.data = data

    @abstractmethod
    def encode(self):
        """Return an encoded version of `self.data` that can be sent over a socket."""
        pass

    @abstractmethod
    def decode(self):
        """Should be able to decode whatever the output of encode() produces and store it in `self.data`"""
        pass


class ConnectionRequestPacket(Packet):
    pass


class ConnectionAcknowledgePacket(Packet):
    pass


class MessagePacket(Packet):
    pass


class UserReportPacket(Packet):
    pass
