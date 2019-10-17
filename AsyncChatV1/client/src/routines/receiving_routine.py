import socket


def receiving_routine(main_socket: socket.socket):
    while True:
        msg = main_socket.recv(1024)
        msg = msg.decode('utf-8')
        print(msg)
