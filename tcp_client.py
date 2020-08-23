import socket

target_host = 'www.google.com'
target_port = 80

# create socket object
# AF_INET is setting for IPv4
# SOCK_STREAM is setting for using TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect server
client.connect((target_host, target_port))

# send data
client.send('GET / HTTP/1.1\r\nHost: google.com\r\n\r\n'.encode())


# receive data
response = client.recv(4096)

print(response)