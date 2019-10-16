import socket

def receiving_thread(main_socket: socket.socket):
    while True:
        msg = main_socket.recv(1024)
        print(msg)