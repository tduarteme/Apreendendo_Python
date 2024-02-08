"""Desenvolva uma solução, que leia um número Real qualquer no teclado
    e mostre na tela a sua porção inteira."""

#import math - > Maneira de importar a biblioteca como um todo.

# Da forma a seguir, importamos um módulo em específico.

from math import trunc
num = float(input(" Digite um número real: "))

#inteira = math.trunc(num)

inteira = trunc(num)
print("A parte inteira do número digitado é {}." .format(inteira))