#!/usr/bin/python
import socket

print ("Interagindo com Servidor FTP")
ip = input("Digite o Endereço IP/URL:")
porta = 21

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meusocket.connect((ip,porta))
banner = meusocket.recv(1024)
print (banner)

print ("Enviando Usuário")
meusocket.send("USER felipe\r\n")
banner = meusocket.recv(1024)
print (banner)

print ("Enviando Senha")
meusocket.send("PASS felipe\r\n")
banner = meusocket.recv(1024)
print (banner)
