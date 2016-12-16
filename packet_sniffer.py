
import socket
from struct import *

try
    s = socket.socket(socket.AF_IPX, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error , msg:
    print 'Socket could not be created. Error Code : ' str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

# receive a packet
while True:
    packet = s.recvfrom(65565)

    packet = packet[0]

    ip_header = packet[0:20]

    pih = unpack('!BBHHHBBH4s4s', ip_header)
    