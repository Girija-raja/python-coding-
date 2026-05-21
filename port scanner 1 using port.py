import socket
s=socket.socket()
s.settimeout(1)
status=s.connect_ex(("127.0.0.1",8080d))
print("port 8080 is OPEN" if status==0 else "port 8080 is CLOSED")
