import threading

from routines import establish_connection, receiving_routine, forwarding_routine


def main():
    main_socket = establish_connection.establish_connection('127.0.0.1', 8088)
    receiving = threading.Thread(target=receiving_routine.receiving_routine, args=(main_socket,))
    receiving.start()

    sending_routine = threading.Thread(target=forwarding_routine.forwarding_routine, args=(main_socket,))
    sending_routine.start()


if __name__ == '__main__':
    main()
