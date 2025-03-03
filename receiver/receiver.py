import socket

def print_key_press(key):
    print(f"Received key: {key}")

def start_receiver(host, port):
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiver_socket.bind((host, port))
    receiver_socket.listen(1)
    print(f"Listening on {host}:{port}...")

    conn, addr = receiver_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        key = data.decode()
        print_key_press(key)

if __name__ == "__main__":
    HOST = '0.0.0.0'  # Listen on all interfaces
    PORT = 12345      # Port to forward on your router

    start_receiver(HOST, PORT)