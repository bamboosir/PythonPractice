import threading
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


def serRsp(tcpCliSock):
    while True:
        data = input(ctime,'>')
        if not data:
            continue
        tcpCliSock.send(data.encode(encoding='utf-8'))
        print(ctime,'[send]',data)

def serRecv(tcpCliSock):
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            continue
        print(ctime(), '[recv]', data)


def startServ():
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)
    isServStarted = False

    while True:
        print('waiting for connection...')
        tcpCliSock, addr = tcpSerSock.recv(BUFSIZ)
        print('connected from ', addr)
        if isServStarted == False:
            rsp = threading.Thread(target=serRsp, args=tcpCliSock)
            rcv = threading.Thread(target=serRecv, args=tcpCliSock )
            rsp.start()
            isServStarted=True
        isRspStarted = False



