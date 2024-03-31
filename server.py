import socket

sock = socket.socket()
sock.bind(('', 9090))
print("Server starting!")
sock.listen(0)
print("Port is listing")
conn, addr = sock.accept()
print("Client accepted")
print("Client adress: ", addr[0])
print("Client port:", addr[1])

msg = ''

while True:
	data = conn.recv(1024)
	if not data:
		break
	msg += data.decode()
	conn.send(msg.upper().encode())

print(msg)

conn.close()
