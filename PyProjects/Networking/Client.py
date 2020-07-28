import socket

HEADER = 64
PORT = 5050
SERVER = '192.168.1.14'#socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
print(ADDR)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECTED"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hola Server")
input()
send("Hello Mate!")
send(DISCONNECT_MESSAGE)
