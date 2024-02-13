"""Desenvolva uma solução que conceda um aumento de 10% aos salários superiores ou igual a R$1.250,00 e 15% aos inferiores."""


salario = float(input("informe o salário: "))

if salario >= 1250:
    bonus = salario + (salario*10/100)

else:
    bonus = salario + (salario*15/100)

print("Seu novo salário é de R$ {:.2f}".format(bonus))