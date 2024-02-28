"""Desenvola um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente."""

from math import cos,tan,sin,radians
angulo = float(input(" Digite o Ângulo desejado: "))

cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))

print("O Cosseno correspondete a este ângulo, é {:.2f}".format(cosseno))
print("O SENO correspondente a este ângulo, é {:.2f}".format(seno))
print("A Tangente correspondente a este ângulo, é {:.2f}" .format(tangente))