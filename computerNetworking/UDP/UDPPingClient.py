#!/usr/bin/env python3  
# encoding: utf-8  
"""
@author: crkylin
@contact: crkylin@gmail.com 
@site:  
@file: UDPPingClient.py 
@time: 4/9/2018 9:10 PM 
"""  
from socket import *
serverName = '127.0.0.1'
serverPort = 23333
serverAddr = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)
msg = input('entry:')
clientSocket.sendto(msg.encode('utf8'), serverAddr)
reponseMsg, addr = clientSocket.recvfrom(1024)
print(reponseMsg)
clientSocket.close()