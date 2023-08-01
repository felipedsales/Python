#!/usr/bin/python
import sys
import os

#Trabalhando com Argumentos 

#Comando para Pegar os Argumentos Passados
print ("Varrendo o Host:",sys.argv[1], "na Porta:",sys.argv[2])

#Utilizando Comandos do Sistema Operacional
print ("Verificando Portas Abertas")
os.system("netstat -nltp")
print ("Listando Arquivos")
os.system ("ls -la")
