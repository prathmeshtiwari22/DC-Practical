import socket

# Your local IP and port
HOST = '192.167.0.186'  # Local IP address of your PC
PORT = 5050             # Custom port

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

with conn:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Received:", data.decode())
        conn.sendall(data)

print("Server closed.")
