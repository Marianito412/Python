import socket

hostname = socket.gethostname()
port = 1324

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((hostname, port))
print(hostname)
s.listen(5)
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
