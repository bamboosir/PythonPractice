import threading
from socket import *
from time import ctime

HOST = '192.168.0.105'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


def cliRsp(tcpCliSock):
    print("cliRsp called")
    while True:
        data = input('>')
        if not data:
            continue
        tcpCliSock.send(data.encode(encoding='utf-8'))
        print(ctime(),'\n[send]',data)

def cliRecv(tcpCliSock):
    print("cliRecv called")

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(ctime(), '\n[recv]', data)


def startClient():
    #HOST = str(input('please enter server IP:'))
    PORT = 21568
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    isClntRspStarted = False

    recv = threading.Thread(target=cliRecv, args=[tcpCliSock])
    rsp = threading.Thread(target=cliRsp, args=[tcpCliSock])

    recv.start()
    rsp.start()

if __name__ == "__main__":
    startClient()

