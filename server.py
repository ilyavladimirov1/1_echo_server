import socket
import logging

# Настройка логгера
logging.basicConfig(filename='server.log', level=logging.INFO)
logger = logging.getLogger('server')

sock = socket.socket()
sock.bind(('', 9090))
logger.info("Server starting!")
sock.listen(0)
logger.info("Port is listening")
conn, addr = sock.accept()
logger.info(f"Client accepted from {addr[0]}:{addr[1]}")


while True:
	data = conn.recv(1024)
    	if not data:
        	break
	logger.info(f"Received message: {data.decode()}")
    	conn.send(data.upper())

conn.close()
