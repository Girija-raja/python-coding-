import socket
import os
s=socket.socket()
s.settimeout(5)
status=s.connect_ex(("127.0.0.1",8080))
if status==0:
    print("port 8080 is OPEN")
else:
    print("port 8080 is CLOSED")
    print(f"Error code:{status}")
    print(f"Reason:{OS.strerror(status)}")
