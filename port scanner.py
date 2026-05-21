import socket
 
s = socket.socket()
 
s.settimeout(1)
 
status = s.connect_ex(("127.0.0.1", 8080))
 
if status == 0:
	print("[+] Port 8080 is OPEN")
else:
	print(f"[-] Port 8080 is CLOSED | Error Code: {status}")
