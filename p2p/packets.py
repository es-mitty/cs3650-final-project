from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

class Packet(ABC):
    def __init__(self, data: dict[str, Any]):
        self.data = data

    @abstractmethod
    def encode(self):
        """Return an encoded version of `self.data` that can be sent over a socket."""
        pass

    @abstractmethod
    @property
    def data(self) -> dict:
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