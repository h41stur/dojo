#!/usr/bin/python3

'''
2 - Crie um programa em python que se conecta via
socket na porta 443 e envia a frase "Hacking Dojo",
entao faça com que este programa seja executado
dentro da VM do Windows 10 envie a frase para o handler.
'''

import socket
import sys

host = "192.168.0.188"
port = 443

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(b"Hacking Dojo\r\n")
s.close()
