"""Desenvolva uma solução que leia o comprimento de 3 regras,
mostre na tela se é possível criar um triângulo entre elas.

Obs.: Só é possível formar um triângulo, se a soma entre dois segmentos forem menor do que o terceiro."""

from time import sleep
r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))

print("CALCULANDO ...")
sleep(4)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Esses Segmentos, foram um TRIÂNGULO!")
else:
    print("Esses segmentos, NÃO foram um TRIÂNGULO")