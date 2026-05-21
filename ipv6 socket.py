import socket
 
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
 
s.connect(("fe80::1856:5cbb:d7a9:777%18", 8080))
 
print("Connected to local IPv6 Apache server")

