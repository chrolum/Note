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
serverPort = 8081
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server is running")
while True:

    connctionSocket, addr = serverSocket.accept()
    try:
        message = connctionSocket.recv(1024)
        fileName = message.split()[1]
        f = open(fileName[1:])
        outputdata = f.read()
        print(outputdata)
        # Send one HTTP header line into socket
        http_response = b"HTTP/1.1 200 OK\r\n\r\n"
        # Send the content of the requeted file to the client
        connctionSocket.sendall(http_response + outputdata.encode("utf8"))
        connctionSocket.close()

    except IOError:
        # Send response message for file not found
        http_response = b'HTTP/1.1 404 Not Found\r\n\r\n'
        f = open('404.html')
        outputdata = f.read()
        connctionSocket.send(http_response + outputdata.encode("utf8"))

        connctionSocket.close()


#DONE! v1.0.1
#Fix the problem that the server down after a connection close DONE:Do not close the welcome socket after a loop
