import socket
import json

port = 5010 # port to listen
print("listening port " + str(port))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind(('',port))

nodes = []

while True:
        in_msg, addr = sock.recvfrom(1024)
        if addr not in nodes:
                nodes.append(addr)
                print('new client: ' + str(addr))

        for node in nodes:
                sock.sendto(json.dumps(list(filter(lambda x: x != node, nodes))).encode('utf-8'), node)
