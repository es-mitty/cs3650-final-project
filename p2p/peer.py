from __future__ import annotations

import socket
from socket import socket as SocketObject
import threading

# source for demo is https://medium.com/@luishrsoares/implementing-peer-to-peer-data-exchange-in-python-8e69513489af


class Peer:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(0.5)
        self.connections: set[SocketObject] = set()
        self.listening = threading.Event()
        self.listening.clear()
    
    def connect(self, peer_host, peer_port):
        connection_names = {
            connection.getpeername(): connection for connection in self.connections
        }
        if (peer_host, peer_port) not in connection_names:
            connection = socket.create_connection((peer_host, peer_port))
            self.connections.add(connection)
            print(f"Connected to {peer_host}:{peer_port}")
            return connection
        else:
            return connection_names[(peer_host, peer_port)]

    def listen(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(10)
        print(f"Listening for connections on {self.host}:{self.port}")

        while self.listening.is_set():
            try:
                connection, address = self.socket.accept()
                self.connections.add(connection)
                print(f"Accepted connection from {address}")
                handler_thread = threading.Thread(
                    target=self.handle_client, args=(connection, address)
                )
                handler_thread.start()
            except TimeoutError:
                pass

    def send_data(self, data, dest_connection: socket.socket | None = None):
        if dest_connection is None:
            for connection in self.connections:
                try:
                    connection.sendall(data.encode())
                except socket.error as e:
                    print(f"Failed to send data. Error: {e}")
                    self.connections.remove(connection)
        else:
            connection = dest_connection
            try:
                connection.sendall(data.encode())
            except socket.error as e:
                print(f"Failed to send data. Error: {e}")
                self.connections.remove(connection)

    def handle_client(self, connection, address):
        while self.listening.is_set():
            try:
                data = connection.recv(1024)
                if not data:
                    break
                print(f"Received data from {address}: {data.decode()}")
            except:
                break

        print(f"Connection from {address} closed.")
        self.connections.remove(connection)
        connection.close()

    def start(self):
        listen_thread = threading.Thread(target=self.listen)
        self.listening.set()
        listen_thread.start()

    def stop(self):
        self.listening.clear()