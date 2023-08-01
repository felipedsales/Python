#!/usr/bin/python
import sys

#Trabalhando com Condições - IF
if len(sys.argv) <=2:
	print ("Modo de Uso: condic.py + IP + PORTA")
	print ("Exemplo de Uso: condic.py 192.168.0.1 80")
else:
	print ("Varrendo o Host:",sys.argv[1], "na Porta:",sys.argv[2])

#Trabalhando com Condições - FOR

for ip in range(1,255):
	print ("Varrendo IP: 192.168.0.%s" %ip)
