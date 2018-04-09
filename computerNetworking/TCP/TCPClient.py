#!/usr/bin/env python3  
# encoding: utf-8  
"""
@author: crkylin
@contact: crkylin@gmail.com 
@site:  
@file: TCPClient.py 
@time: 4/3/2018 2:11 PM 
"""  
from socket import *
serverName = '127.0.0.1'
serverPort = 23333
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('plz input the sentence:')
clientSocket.send(bytes(message, 'ascii'))
modifiedmsg = clientSocket.recv(1024)
print(modifiedmsg)
clientSocket.close()