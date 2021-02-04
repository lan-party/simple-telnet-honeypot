import socket

HOST = '127.0.0.1'
PORT = 23

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            conn.send(b'BusyBox on localhost login: ')
            username = ""
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                if data == b'\r\n':
                    print(username)
                    conn.send(b'Password: ')
                    password = ""
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        conn.sendall(b'\b \b')
                        if data == b'\r\n':
                            print(password)
                            break
                        password += data.decode("utf-8")
                    break
                username += data.decode("utf-8")
