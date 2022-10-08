import socket


def client():
    try:
        host = socket.gethostname()
        port = 8080

        client_socket = socket.socket()
        client_socket.connect((host, port))
        while True:
            message = input('--> ')
            if message.lower().strip() == 'bye':
                print('bye!')
                break
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            print(f'{data}')

            client_socket.close()
    except ConnectionRefusedError:
        print('Server is not running')

if __name__ == '__main__':
    client()
