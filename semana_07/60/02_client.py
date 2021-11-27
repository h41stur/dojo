#!/usr/bin/python3

'''
2 - Crie um programa em python que se conecta via
socket na porta 443 e envia a frase "Hacking Dojo",
entao faça com que este programa seja executado
dentro da VM do Windows 10 envie a frase para o handler.
'''

import socket
import ssl

server_crt = 'server.crt'

host = "192.168.0.188"
port = 443

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_client = ssl.wrap_socket(s, ca_certs=server_crt, cert_reqs=ssl.CERT_REQUIRED)
ssl_client.connect((host, port))
ssl_client.write(b"Hacking Dojo\r\n")