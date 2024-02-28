"""Desenvolva um programa que leia duas notas, calcule e mostre a média."""

n1 = float(input("NOTA 1: "))
n2 = float(input("NOTA 2: "))

m = (n1+n2)/2

print("A média das notas {} e {}, é {:.1f}." .format(n1, n2, m))

# Este comando ":.1f", refere-se a quantidade de dígitos após a vírgula, posso utilizar quantos quiser.