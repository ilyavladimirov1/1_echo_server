import socket

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))

while True:
    msg = input("Your string (type 'exit' to quit): ")
    sock.send(msg.encode())
    if msg.strip() == 'exit':
        break
    data = sock.recv(1024)
    print(data.decode())

sock.close()
