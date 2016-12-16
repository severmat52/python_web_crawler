
import socket

s = socket.socket(socket.AF_IPX, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True:
    print(s.recvfrom(65565))