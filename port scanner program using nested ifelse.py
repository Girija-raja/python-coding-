import socket
s=socket.socket()
s.settimeout(5)
status=s.connect_ex(("127.0.0.1",8080))
if status==0:
    print("Poet 8080 is OPEN")
else:
    print("Port is CLOSED")
    print(f"Error code:{status}")
if status==10061:
    print("Reason:Connection Refused")
elif status==10060:
    print("Reason:Connection Timed Out")
elif status==10035:
    print("Reason:Operation Would Block")
else:
    print("Reason:Unknown")
