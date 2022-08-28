import socket


def main():
    host = socket.gethostname()
    port = 8080

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print(f'Connection from {address}')
    while True:
        data = conn.recv(100).decode()

        if not data:
            break
        print(f'Data: {data}')
        message = (f'Received message: {data}\n'
                   f'bye!')
        conn.send(message.encode())
    conn.close()


if __name__ == '__main__':
    main()
