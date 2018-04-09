#!/usr/bin/env python3  
# encoding: utf-8  
"""
@author: crkylin
@contact: crkylin@gmail.com 
@site:  
@file: webserver.py 
@time: 4/3/2018 3:02 PM 
"""
#import socket module
from socket import *
#Create a welcome socket
serverPort = 23333
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    print("Server is running")
    connctionSocket, addr = serverSocket.accept()
    try:
        message = connctionSocket.recv(1024)
        fileName = message.split()[1]
        f = open(fileName[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        header = 'HTTP/1.1 200 OK'
        connctionSocket.send(header.encode("utf8"))
        print("1")
        # Send the content of the requeted file to the client
        for i in range(0, len(outputdata)):
            connctionSocket.send(outputdata[i].encode("utf8"))
        connctionSocket.close()

    except IOError:
        # Send response message for file not found
        responseMsg = 'HTTP/1.1 404 Not Found'
        connctionSocket.send(responseMsg)
        connctionSocket.close()

    serverSocket.close()
