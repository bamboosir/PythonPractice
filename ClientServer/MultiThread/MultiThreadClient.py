import threading
from socket import *
from time import ctime

HOST = '192.168.0.105'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


def cliRsp(tcpCliSock):
    while True:
        data = input('>')
        if not data:
            continue
        tcpCliSock.send(data.encode(encoding='utf-8'))
        print(ctime(),'[send]',data)

def cliRecv(tcpCliSock):
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(ctime(), '[recv]', data)


def startClient():
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    isClntRspStarted = False

    recv = threading.Thread(target=cliRecv, args=tcpCliSock)
    rsp = threading.Thread(target=cliRsp, args=tcpCliSock)



