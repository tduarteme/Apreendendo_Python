"""Desevolva uma solução, que leia o nome completo de uma pessoa e atenda as exigências abaixo:

Todas as Letras Maiúsculas e minúsculas
Quantas letras ao todo (sem contar os espaços)
Quantas letras tem o primeiro nome"""

nome = str(input("Digite seu Nome Completo: ")).strip()
dividido = nome.split()

print ("Seu nome em Maiúsculo: {}".format(nome.upper()))
print ("Em Minúsculo: {}".format(nome.lower()))
print ("Seu nome possuí {} letras: ".format(len(nome) - nome.count(" ")))
print ("Seu primeiro nome é {}, possuí {} letras: ".format(dividido[0], len(dividido[0])))

