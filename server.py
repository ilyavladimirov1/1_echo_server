import socket

sock = socket.socket()
sock.bind(('', 9090))
print("Server starting!")
sock.listen(0)
print("Port is listening")
conn, addr = sock.accept()
print("Client accepted")
print("Client address:", addr[0])
print("Client port:", addr[1])


while True:
	data = conn.recv(1024)
    	if data.decode().strip() == 'exit':
        	break
    	conn.send(data.upper())

conn.close()
