from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any
from enum import Enum


class PacketType(Enum):
    CONNECTION_REQUEST = 0
    CONNECTION_ACK = 1
    MESSAGE = 2
    REPORT = 3


class Packet(ABC):

    type: PacketType

    def __init__(self, data: dict[str, Any]):
        self.data = data

    @abstractmethod
    def encode(self):
        """Return an encoded version of `self.data` that can be sent over a socket."""
        pass


class ConnectionRequestPacket(Packet):
    pass


class ConnectionAcknowledgePacket(Packet):
    pass


class MessagePacket(Packet):
    pass


class UserReportPacket(Packet):
    pass


class RawPacketDecoder:
    @staticmethod
    def decode_raw_packet() -> Packet:
        pass