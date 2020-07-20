## P2P-UDP-example

It's just a simple P2P-UDP example written in Python3.
To get it working put `udp_server.py` in a host with a static address. The server is needed to initialize the connection between UDP nodes by storing the node's addresses.

Then run several instances of `udp_node.py` to see the exchange with hello-datagrams.
