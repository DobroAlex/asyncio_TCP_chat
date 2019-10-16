import threading

from routines import establish_connection, receiving_thread


def main():
    main_socket = establish_connection.establish_connection('127.0.0.1', 8088)
    receiving = threading.Thread(target=receiving_thread.receiving_thread, args=(main_socket,))
    receiving.start()


if __name__ == '__main__':
    main()
