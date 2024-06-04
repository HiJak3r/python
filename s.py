#!/bin/python3

# SOCKETS

import socket

HOST = '127.0.0.1'
PORT = 7777

# We define s since we don't want to keep typing it
# The actual command just specifies that the socket command will use IPv4 and a certain port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, sock_stream is a port

# This will actually attempt to make the connection over the specified IP and port
s.connect((HOST,PORT))
