import socket
import json
from time import sleep

host = '141.8.198.24' # server ip
port = 5010
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

nodes = [] # all nodes in network

out_msg = "hello"

while True:
	sock.sendto(out_msg.encode('utf-8'),(host, port))
	in_msg, addr = sock.recvfrom(1024)

	# if message from server then update nodes, else do multicast sending
	if (addr[0] == host):
		nodes = json.loads(in_msg.decode('utf-8'))
	else:
		print('new message: ' + in_msg.decode('utf-8') + ' from: ' + str(addr))

	for node in nodes:
		sock.sendto(out_msg.encode('utf-8'), (node[0], node[1]))
	sleep(5)
