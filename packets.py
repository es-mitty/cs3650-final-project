from abc import ABC, abstractmethod
from typing import Any
from dataclasses import dataclass


class Packet(ABC):
    def __init__(self, data: dict[str, Any]):
        self.data = data

    @abstractmethod
    def encode(self):
        pass

    @abstractmethod
    def decode(self):
        pass


class ConnectionRequestPacket(Packet):
    pass


class ConnectionAcknowledgePacket(Packet):
    pass


class MessagePacket(Packet):
    pass


class UserReportPacket(Packet):
    pass
