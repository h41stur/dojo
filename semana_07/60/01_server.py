#!/usr/bin/python3

'''
1 - Crie um programa em python utilizando socket que inicia um handler
na porta 443, ou seja um processo que espera uma conexão na porta 443.
Então deixe-o escutando no Kali.
'''

import socket
import sys
import ssl

lhost = "0.0.0.0"
lport = 443
buff = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((lhost,lport))
server.listen(10)

print("[+] Iniciando handler!")

while True:
    clientsocket, clientaddr = server.accept()
    print("[+] Recebendo conexao de " + clientaddr[0])
    ssl_server = ssl.wrap_socket(clientsocket, server_side=True, certfile="server.crt", keyfile="server.key",
                                        ssl_version=ssl.PROTOCOL_TLSv1)
    data = ssl_server.read()
    data = data.decode()
    print(data)
#    while True:
#        resp = input("")
#        if resp == "exit":
#            server.close()
#            sys.exit()
#        clientsocket.sendall(resp + b"\n")
#        try:
#            data = clientsocket.recv(buff)
#            data = data.decode()
#            print(data)
#        except:
#            pass


