#!/usr/bin/env python3  
# encoding: utf-8  
"""
@author: crkylin
@contact: crkylin@gmail.com 
@site:  
@file: UDPPingServer.py 
@time: 4/9/2018 9:09 PM 
"""  
from socket import *
import random
serverPort = 23333
serverAddr = ('', serverPort)
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(serverAddr)

while True:
    rand = random.randint(0 ,10)
    msg, addr = serverSocket.recvfrom(1024)
    msg = msg.upper()

    if rand < 4:#suimulate the situation of losting package
        continue

    serverSocket.sendto(msg, addr)
