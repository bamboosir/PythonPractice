#!/usr/bin/env python
#encoding ='utf-8'


from socket import *


HOST = '192.168.0.105'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpClickSock = socket(AF_INET, SOCK_STREAM)
tcpClickSock.connect(ADDR)

while True:
    data = str(input('>'))
    #print(type(data))
    if not data:
        break
    data = data.encode(encoding="utf-8")
    #print(type(data))
    tcpClickSock.send(data)
    data = tcpClickSock.recv(BUFSIZ)
    if not data:
        break
    print('client recv data from ser')
    print(data)

tcpClickSock.close()



