import socket
s=socket(socket.AF_INET, socket.SOCK_STREAM)
s.bing('0.0.0.0', 9999)
s.listen(1)
while True:
    client, address = s.accept()
while True:
    data = client.recv(1024)
    if not data:
        break
    if data == 'Close' or 'close':
        client.close()
client.send(data)
client.close()
