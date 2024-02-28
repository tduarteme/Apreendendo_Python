"""Faça um programa que leia um número de 0 a 9999, mostre na tela cada dígito separado.
Unidade, Dezena, Centena, Milhar"""


numero = int(input("Digite um valor inteiro: "))

uni = numero //1 % 10
dez = numero //10 % 10
cen = numero //100 % 10
mil = numero //1000 % 10

print ("Unidade: {}" .format(uni))
print ("Dezena: {}".format(dez))
print ("Centena: {}".format(cen))
print ("Milhar: {}" .format(mil))

