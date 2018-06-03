from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection..')
    tcpCliSock, addr = tcpSerSock.accept()
    print('..connected from', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(ctime(),'[recv] ',addr, data)

        while True:
            data = input('>')
            if not data:
                print('input error, please try again')
                continue
            else:
                print(ctime(), '[send]',data)
                tcpCliSock.send(data.encode(encoding='utf-8'))
                break

print('fish')

tcpCliSock.close()
tcpSerSock.close()