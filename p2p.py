import socket
import threading
import time

# source for demo is https://medium.com/@luishrsoares/implementing-peer-to-peer-data-exchange-in-python-8e69513489af

class Peer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []

    def connect(self, peer_host, peer_port):
        connection = socket.create_connection((peer_host, peer_port))

        self.connections.append(connection)
        print(f"Connected to {peer_host}:{peer_port}")

    def listen(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(10)
        print(f"Listening for connections on {self.host}:{self.port}")

        while True:
            connection, address = self.socket.accept()
            self.connections.append(connection)
            print(f"Accepted connection from {address}")
            threading.Thread(target=self.handle_client, args=(connection, address)).start()

    def send_data(self, data):
        for connection in self.connections:
            try:
                connection.sendall(data.encode())
            except socket.error as e:
                print(f"Failed to send data. Error: {e}")
                self.connections.remove(connection)

    def handle_client(self, connection, address):
        while True:
            try:
                data = connection.recv(1024)
                if not data:
                    break
                print(f"Received data from {address}: {data.decode()}")
            except socket.error:
                break

        print(f"Connection from {address} closed.")
        self.connections.remove(connection)
        connection.close()

    def start(self):
        listen_thread = threading.Thread(target=self.listen)
        listen_thread.start()




if __name__ == "__main__":
    anja_port = 8000
    makayla_port = 8001
    eli_port = 8002
    murphy_port = 8003

    Anja = Peer("0.0.0.0", 8000)
    Anja.start()

    Makayla = Peer("0.0.0.0", 8001)
    Makayla.start()

    Eli = Peer("0.0.0.0", 8002)
    Eli.start()

    Murphy = Peer("0.0.0.0", 8003)
    Murphy.start()

    time.sleep(2)


    quit_demo = "continue"
    while(quit_demo != "quit"):
        source = input("Type who you are: ")
        dest = input("Type who you want to send to: ")
        message = "https://api.thecatapi.com/v1/images/search?api_key=live_pGPtu252IVJfrslX8KvUkqhFOmid15pf8qL7r2PqXiPlnEwYzg7JWGC2MZdwTW4u"

        if source == "Anja":
            if dest == "Makayla":
                Anja.connect("127.0.0.1", makayla_port)
            elif dest == "Eli":
                Anja.connect("127.0.0.1", eli_port)
            elif dest == "Murphy":
                Anja.connect("127.0.0.1", murphy_port)
            time.sleep(2)
            Anja.send_data(message)
            
        elif source == "Makayla":
            if dest == "Anja":
                Makayla.connect("127.0.0.1", anja_port)
            elif dest == "Eli":
                Makayla.connect("127.0.0.1", eli_port)
            elif dest == "Murphy":
                Makayla.connect("127.0.0.1", murphy_port)
            time.sleep(2)
            Makayla.send_data(message)


        elif source == "Eli":
            if dest == "Anja":
                Eli.connect("127.0.0.1", anja_port)
            elif dest == "Makayla":
                Eli.connect("127.0.0.1", makayla_port)
            elif dest == "Murphy":
                Eli.connect("127.0.0.1", murphy_port)
            time.sleep(2)
            Eli.send_data(message)

        elif source == "Murphy":
            if dest == "Makayla":
                Murphy.connect("127.0.0.1", makayla_port)
            elif dest == "Eli":
                Murphy.connect("127.0.0.1", eli_port)
            elif dest == "Anja":
                Murphy.connect("127.0.0.1", anja_port)
            time.sleep(2)
            Murphy.send_data(message)

        quit_demo = input("Type quit to quit the demo or anything else to continue: ")
        



