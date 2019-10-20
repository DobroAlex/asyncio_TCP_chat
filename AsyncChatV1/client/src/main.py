import threading

from classes import stoppable_thread

from routines import establish_connection, receiving_routine, forwarding_routine


def main():
    main_socket = establish_connection.establish_connection('127.0.0.1', 8088)

    receiving = threading.Thread(target=receiving_routine.receiving_routine, args=(main_socket,), daemon=True)

    sending = threading.Thread(target=forwarding_routine.forwarding_routine, args=(main_socket,), daemon=True)

    running_threads = (receiving, sending)

    for thread in running_threads:
        thread.start()

    while True:
        for thread in running_threads:
            if not thread.is_alive():
                print(f'Thread {thread.name} is dead, aborting execution')
                return


if __name__ == '__main__':
    main()
