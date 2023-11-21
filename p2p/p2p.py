from __future__ import annotations

import time

from peer import Peer
from typing import TypedDict

class UserEntry(TypedDict):
    port: int
    peer: Peer

def main() -> None:
    ESTABLISHING_IPV4_ADDR = "0.0.0.0"
    CONNECTION_IPV4_ADD = "127.0.0.1"
    users: dict[str, UserEntry] = {
        "Anja": {"port": 8000, "peer": None},
        "Makayla": {"port": 8001, "peer": None},
        "Eli": {"port": 8002, "peer": None},
        "Murphy": {"port": 8003, "peer": None},
    }

    for user in users:
        peer = Peer(ESTABLISHING_IPV4_ADDR, users[user]["port"])
        peer.start()
        users[user]["peer"] = peer

    time.sleep(0.5)

    quit_demo = "continue"
    while quit_demo != "quit":
        source = input("Type who you are: ")
        dest = input("Type who you want to send to: ")
        message = "https://api.thecatapi.com/v1/images/search?api_key=live_pGPtu252IVJfrslX8KvUkqhFOmid15pf8qL7r2PqXiPlnEwYzg7JWGC2MZdwTW4u"

        if source in users and dest in users:
            source_peer: Peer = users[source]["peer"]
            connection  = source_peer.connect(CONNECTION_IPV4_ADD, users[dest]["port"])
            time.sleep(0.5)
            source_peer.send_data(message, connection)
            time.sleep(0.5)

        quit_demo = input("Type quit to quit the demo or anything else to continue: ")

    for key, user in users.items():
        user["peer"].stop()
        print(f"Stopping peer: {key}")

if __name__ == "__main__":
    main()
