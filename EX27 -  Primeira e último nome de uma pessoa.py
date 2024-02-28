"""Faça um programa que leia o nome completo, mostrando o primeiro e último nome separados
EX.: Thiago Duarte
     primeiro = Thiago
     último = Duarte"""

nome = str(input("Informe seu Nome Completo: ")).strip().split()
print("Olá, é um prazer te conhecer")


print("Seu primeiro nome é {}".format(nome[0]))
print("Seu último nome é {}".format(nome[len(nome)-1]))