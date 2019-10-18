import socket
import jsonpickle

def receiving_routine(main_socket: socket.socket):
    while True:
        msg = main_socket.recv(1024)

        msg = msg.decode('utf-8')
        msg = msg.replace('\n', ' ').replace('\r', ' ')

        msg = jsonpickle.decode(msg)
        print(msg)
