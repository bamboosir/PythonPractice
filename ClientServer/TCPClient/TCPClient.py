#!/usr/bin/env python
#encoding ='utf-8'


from socket import *
from time import ctime

HOST = '192.168.0.105'
PORT = 21567
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
    tcpClickSock.send(data)
    print(ctime(),'[send]',data)

    data = tcpClickSock.recv(BUFSIZ)
    if not data:
        break
    print(ctime(),'[recv]',data)


print('connect finish')

tcpClickSock.close()



