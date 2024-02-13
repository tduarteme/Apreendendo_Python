"""Crie um programa que leia qualquer ano, mostre se ele é BISSEXTO ou não."""

from datetime import date

ano = int(input("Informe o ano que deseja analisar ou pressione 0 para saber o ano atual: "))
if ano == 0:
    ano = date.today().year # Este módulo mostra o ano atual.

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é BISSEXTO.".format(ano))

else:
    print("Este ano não é BISSEXTO.")