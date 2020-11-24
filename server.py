# -*- coding: utf-8 -*-
"""
Spyder Editor

Created on Tue Nov 24 06:31:01 2020

@author: ISREAL UFUMAKA

import socket

s = socket.socket()
host = socket.gethostname()
port = 65432
s.bind((host, port))

s.listen(5)
while True:
    conn, addr = s.accept()
    print("We have a connection from ", addr)
    conn.send("Thank you for connecting")
    conn.close()
    
"""
# we import the python socket library
import socket 

# creating a python socket object we would make a connection to
s = socket.socket() 
# get the local machine name, you can just specify the ip machine adress 127.0.0.1
host = socket.gethostname() 
# port to listen for
port = 65432
# bind address to port
s.bind((host, port)) 
#  now wait for connection
s.listen(5)
while True:
    #  establishing an active connection with client
    con, addr = s.accept()
    with con:
        print("We have a connection from ", addr)
        while True:
            data = con.recv(1024)
            if not data:
                break
            con.sendall(data)
             # closing the previously established connection
        con.close() 


"""EXPLAINATION OF THE INNER LOOPING
with con:
        print("We have a connection from ", addr)
        while True:
            data = con.recv(1024)
            if not data:
                break
            con.sendall(data)
            
We actually use an infinity loop to communicate with con.recv(),
and this actually reads whatever the client sends and echos it back directly
using con.sendall(). 
The WITH allows our script close connection automatically.
NOTE: if an empty byte is returned i.e. from as b'' from the client,
the connection is closed.
"""