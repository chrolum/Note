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
def main():
    serverName = '127.0.0.1'
    serverPort = 23333
    serverAddr = (serverName, serverPort)
    pingTest(serverAddr, pingTime=10)

def pingTest(serverAddr, pingTime):#ping pingTime to server
    for i in range(0, pingTime):
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        msg = makePingPackage(i)#make ping package
        clientSocket.sendto(msg.encode('ascii'), serverAddr)
        acceptReturnMsg(clientSocket)
        clientSocket.close()

def makePingPackage(time):
    return 'ping' + time + date()


def acceptReturnMsg(clientSocket):
    reponseMsg, addr = clientSocket.recvfrom(1024)  # set timeout to while
    print(reponseMsg)

    
if __name__ == '__main__':
    main()