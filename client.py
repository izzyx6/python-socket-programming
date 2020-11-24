# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 06:31:01 2020

@author: ISREAL UFUMAKA

import socket

s = socket.socket()
host = socket.gethostname()
port = 65432
s.connect((host, port))
print(s.recv(1024))
s.close()

"""

import socket

s = socket.socket()
host = socket.gethostname()
port = 65432
s.connect((host, port))
s.sendall(b"Hello, how are you doing today Mr Server?")
data = s.recv(1024)
print("Received", repr(data))
s.close()

"""
The client script basically makes a connection to the server waiting for
connection and sends a message by calling the s.recv(). The received reply
from the server is then read and outputed on the screen using print.
NOTE: the 'repr' returns the canonical object of a string
"""