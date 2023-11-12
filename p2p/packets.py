from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable
from enum import Enum


class PacketType(Enum):
    CONNECTION_REQUEST = 0xC
    CONNECTION_ACK = 0xA
    MESSAGE = 0xD
    REPORT = 0xF


@dataclass
class Packet(ABC):

    source_address: bytearray
    destination_address: bytearray
    type: PacketType

    def __init__(self, from_bytes: bytearray | None = None):
        if from_bytes:
            assert len(from_bytes) >= 8
            self.source_address = from_bytes[0:4]
            self.destination_address = from_bytes[4:8]


    @abstractmethod
    def encode(self) -> bytearray:
        """Return an encoded version of `self.data` that can be sent over a socket."""
        pass


class ConnectionRequestPacket(Packet):

    type = PacketType.CONNECTION_REQUEST


class ConnectionAcknowledgePacket(Packet):

    type = PacketType.CONNECTION_ACK


class MessagePacket(Packet):
    
    type = PacketType.MESSAGE


class UserReportPacket(Packet):
     
    type = PacketType.REPORT


def packet_factory(from_bytes: bytearray) -> Packet:
    """Given some decoded bytes from a TCP packet, return the appropriate data structure with decoded data."""
    CLASS_MAP: dict[PacketType, Callable] = {
            PacketType.CONNECTION_REQUEST: ConnectionRequestPacket,
            PacketType.CONNECTION_ACK: ConnectionAcknowledgePacket,
            PacketType.MESSAGE: MessagePacket,
            PacketType.REPORT: UserReportPacket,
        }
    
    assert len(from_bytes) >= 9

    packet_type = PacketType(from_bytes[0])
    packet_data = from_bytes[1:]
    return CLASS_MAP[packet_type](from_bytes=packet_data)
