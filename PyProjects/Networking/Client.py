import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = socket.gethostbyname("DESKTOP-1M51O3L")
print(server)
s.connect((server, 1324))
msg = s.recv(1024)
print(msg.decode("utf-8"))