import socket

hostname = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:

s.connect(("8.8.8.8", 80))
ip_address = s.getsockname()[0]
finally:
s.close()
print("Host Name :", hostname)
print("IP Address:", ip_address)

OUTPUT:

Host Name: DESKTOP-PCPHPRB
IP Address: 192.168.3.26
