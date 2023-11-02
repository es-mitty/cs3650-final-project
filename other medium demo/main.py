import socket
import threading

HOST = "127.0.0.1" # windows ip addy
PORT = 60001

def receive_data(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received {data.decode()}")

def send_data(conn):
    while True:
        message = input("Enter a message: ")
        if message.lower() == "quit":
            break
        conn.sendall(message.encode())

# Establish connection as a peer
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Waiting for incoming connections...")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        # Start receiving and sending data concurrently
        recv_thread = threading.Thread(target=receive_data, args=(conn,))
        send_thread = threading.Thread(target=send_data, args=(conn,))
        recv_thread.start()
        send_thread.start()
        recv_thread.join()
        send_thread.join()