
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 8080))

http_request = (
    "GET / HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "Connection: close\r\n"
    "\r\n"
)

client.sendall(http_request.encode())

response = b""

while True:
    chunk = client.recv(1024)

    if not chunk:
        break

    response += chunk

print("--- Received HTTP Response ---")
print(response.decode())

client.close()

OUTPUT:-  
--- Received HTTP Response ---
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Connection: close

<html><body><h1>Welcome to Computer Networks Lab!</h1></body></html>
