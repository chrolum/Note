#!/usr/bin/env python3  
# encoding: utf-8  
"""
@author: crkylin
@contact: crkylin@gmail.com 
@site:  
@file: UDPServer.py 
@time: 4/2/2018 11:01 AM 
"""  
from socket import *
serverPort = 23333
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is runnning")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
