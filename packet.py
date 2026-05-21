from scapy.all import IP, TCP
packet = IP(dst="192.168.1.1") / TCP(dport=80)
print(f"[+] Packet structure: {packet.summary()}")
