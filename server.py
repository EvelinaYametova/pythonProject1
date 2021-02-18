import socket
import dnslib

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.sendto(dnslib.DNSRecord.question("e1.ru").pack(), ('localhost', 53))
server.close()
