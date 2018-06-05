import threading
from socket import *
from time import ctime

BUFSIZ = 1024


def serRsp(tcpCliSock):
    print('serRsp called')
    while True:
        data = input('>')
        if not data:
            continue
        tcpCliSock.send(data.encode(encoding='utf-8'))
        print(ctime(),'\n[send]>',data)

def serRecv(tcpCliSock):
    print('serRecv called')

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            continue
        print(ctime(), '\n[recv]>', data)


def startServ():
    HOST = '192.168.0.105'
    PORT = 21568
    ADDR = (HOST, PORT)

    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    #tcpSerSock.close()
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)
    isServStarted = False

    while True:
        print('waiting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('connected from ', addr)
        if isServStarted == False:
            rsp = threading.Thread(target=serRsp, args=[tcpCliSock])
            rcv = threading.Thread(target=serRecv, args=[tcpCliSock])
            rsp.start()
            rcv.start()
            isServStarted=True
        isRspStarted = False

    tcpCliSock.close()
    tcpSerSock.close()

if __name__ == "__main__":
    startServ()
