from peer import Peer


class Relay(Peer):
    """Relay used for handling all incoming and outgoing traffic in an unstructured P2P network."""
    def __init__(self, host, port):
        super().__init__(host, port)

    def handle_client(self, connection, address):
        """Plan to override to handle relay stuff."""
        return super().handle_client(connection, address)
