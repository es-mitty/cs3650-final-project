from peer import Peer
from typing import Callable
import socket
from packets import *


class Relay(Peer):
    """Relay used for handling all incoming and outgoing traffic in an unstructured P2P network."""

    recv_callback: Callable

    def __init__(self, host, port):
        super().__init__(host, port)

    def handle_client(self, connection, address):
        """Plan to override to handle relay stuff."""
        while True:
            try:
                raw_data = connection.recv(1024)
                if not raw_data:
                    break
                decoded_packet = RawPacketDecoder.decode_raw_packet(raw_data)
                self.route_packet(decoded_packet, connection)
            except socket.error:
                break

        print(f"Connection from {address} closed.")
        self.connections.remove(connection)
        connection.close()

    def route_packet(self, decoded_packet, connection):
        pass

    def set_recv_callback(self, callback: Callable):
        self.recv_callback = callback
