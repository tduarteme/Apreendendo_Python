"""Crie um programa que leia o valor inteiro e apresente na tela se ele é par ou ímpar."""

valor = int(input("Informe um número qualquer: "))
numero = valor % 2
if numero == 0:
    print("O valor {} é PAR".format(valor))
else:
    print("{} é Ímpar".format(valor))