#!/usr/bin/env python3  
# encoding: utf-8  
"""
@author: crkylin
@contact: crkylin@gmail.com 
@site:  
@file: UDPClient.py 
@time: 4/2/2018 10:59 AM 
"""  
from socket import *
serverName = "127.0.0.1"#IP or hostname
serverPort = 23333
clientSocket = socket(AF_INET, SOCK_DGRAM)#AF_INET is IPV4 SOCK_DGRAM is UDP
message = input('Input lowercase sentence:')
clientSocket.sendto(bytes(message, 'ascii'), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage, serverAddress)
clientSocket.close()