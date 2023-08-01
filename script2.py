#!/usr/bin/python
#Primeiro Script em Python

#Print Exibe o Texto na Tela
print ("Aprendendo Python")

#Definindo Variáveis
ip = input("Digite o IP: ")
porta = eval(input("Digite a Porta:"))
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
