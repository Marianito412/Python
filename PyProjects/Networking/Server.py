import socket
import threading
import re

HEADER = 64
PORT = 5050
SERVER = '192.168.1.14'#socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
print(ADDR)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


messages = []

# [192.168.1.14] Marianito

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
            else:
                messages.append(msg)

            print(f"[{addr}] {msg}")
            #conn.send(f"[RECIEVED {addr[0]} {msg}]".encode(FORMAT))

    conn.close()


def serve_message(conn, addr):

    connected = True
    while connected:
        for message in messages:
            print(re.findall("\[(.*?)\]", message)[0], addr[0])

            if re.findall("\[(.*?)\]", message)[0] == addr[0]:
                to_send = re.sub("\[(.*?)\]", "/")
                conn.send(to_send.encode(FORMAT))

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        #start messsage reciever
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        #start messsage sender
        thread2 = threading.Thread(target=serve_message, args=(conn, addr))
        thread2.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    start()