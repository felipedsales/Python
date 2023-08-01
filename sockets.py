#!/usr/bin/python
import socket,sys

ip = input("Digite o IP: ")
porta =int(input("Digite a Porta: "))

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = meusocket.connect_ex((ip,porta))

if (res == 0):
	print ("Porta Aberta")
else:
	print ("Porta Fechada")
