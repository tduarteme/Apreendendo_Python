"""Faça um programa que leia 3 valores, mostre quem é o maior e menor entre eles na tela."""
from time import sleep

a = float(input("Primeiro valor: "))
b = float(input("Segundo valor: "))
c = float(input("Terceiro valor: "))

# Analisando o menor valor!
menor=a

if b<a and b<c:
    menor=b

if c<a and c<b:
    menor=c

# Analisando o maior valor!

maior=a

if b>a and b>c:
    maior=b

if c>a and c>b:
    maior=c

print("Processando ...")
sleep(2)


print("O maior valor digitado foi {:.0f}.".format(maior))

print("Menor valor foi {:.0f}.".format(menor))

