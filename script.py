#!/usr/bin/python
#Primeiro Script em Python

#Print Exibe o Texto na Tela
print ("Hello World")

#Definindo Variáveis
ip = "192.168.0.1"
porta = 80
version = 1.1

#Exibindo Texto e Chamando as Variáveis
print ("Scan Versão:",version)
print ("Varrendo o Host:",ip,"na porta:",porta) 

#Exibe o Tipo de Variável
print ("IP", type (ip))
print ("Porta", type (porta))
print ("Versão", type (version))

#Outra Forma de Exibir Variáveis
print ("Varrendo Host: %s na porta %d" %(ip,porta))
