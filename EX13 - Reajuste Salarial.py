"""Faça um algoritmo que leia o salário, apresente na tela o valor com o reajuste 15% de aumento"""

salario = float(input(" Valor Salário: R$ "))
#reajuste = salario + ((salario*15)/100) -> O cálculo poderá ser feito assim ou da maneira, abaixo.

print(" Parabéns, seu salário teve um aumento de 15%. Passará a valer R$ {:.2f}." .format(salario + (salario*15)/100))