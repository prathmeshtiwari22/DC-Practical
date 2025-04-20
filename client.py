import socket

# Connect to the server's IP and port
HOST = '192.167.0.186'  # Same IP as the server
PORT = 5050             # Must match the server port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = input("Enter message to send: ")
client_socket.sendall(message.encode())

data = client_socket.recv(1024)
print('Received from server:', data.decode())

client_socket.close()
