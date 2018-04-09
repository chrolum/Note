#!/usr/bin/env python3  
# encoding: utf-8  
"""
@author: crkylin
@contact: crkylin@gmail.com 
@site:  
@file: TCPServer.py 
@time: 4/3/2018 2:12 PM 
"""  
from socket import *
serverPort = 23333
serverSocket = socket(AF_INET, SOCK_STREAM)# The welcome socket
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print("Server is running")
while True:
    connectionSocket, addr = serverSocket.accept()
    msg = connectionSocket.recv(1024)
    modifiedmsg = msg.upper()
    connectionSocket.send(modifiedmsg)
    # connectionSocket.close()