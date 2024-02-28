"""Desenvolva um programa que questione a distância de uma viagem em km!
Calcule o custo da passagem, considerando R$0,50 por até 200km, caso contrário será R$0,45. """

distancia = float(input("Qual a distãncia da viagem? "))

passagem = distancia * 0.50
pass_desc = distancia * 0.45

if distancia <=200:
    
    print("Obrigado por nos escolher, o custo da passagem será de R${:.2f}.".format(passagem))

else:
    
    print("Oba, temos um desconto especial para você, se fechar conosco hoje, pagará R${:.2f} e não o valor original de R${:.2f}.".format(pass_desc, passagem))
    