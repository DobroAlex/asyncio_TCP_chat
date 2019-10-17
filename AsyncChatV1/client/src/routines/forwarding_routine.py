def forwarding_routine(main_socket):
    while True:
        msg = input()
        msg = bytearray(msg, 'utf-8')
        main_socket.send(msg)
