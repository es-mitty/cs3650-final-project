from peer import Peer
from typing import Callable


class Relay(Peer):
    """Relay used for handling all incoming and outgoing traffic in an unstructured P2P network."""
    def __init__(self, host, port):
        super().__init__(host, port)
        self.recv_callback = None

    def handle_client(self, connection, address):
        """Plan to override to handle relay stuff."""
        return super().handle_client(connection, address)

    def set_recv_callback(self, callback: Callable):
        self.recv_callback = callback
