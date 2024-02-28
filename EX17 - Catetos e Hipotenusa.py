""" Desenvolva uma solução que leia o comprimento do cateto oposto e do cateto adjacente,
    de um triângulo e retângulo, calcule e mostre o comprimento da hipotenusa."""

from math import hypot  
oposto = float(input("Informe o Cateto Oposto: "))

adjacente = float(input("Informe o Cateto Adjacente: "))

hipotenusa = hypot(oposto, adjacente)
print("O comprimento da hipotenusa corrresponde a {:.2f}".format(hipotenusa))