"""Escreva uma programa que faça o computador "pensar" em um número inteiro,
entre 0 e 5.
   Peça para o usuário tentar descobrir, qual foi o número escolhido pelo computador.
   O programa deverá mostrar na tela, usuário venceu ou perdeu!"""


from random import randint
from time import sleep
jogador = int(input("Tente advinhar o número que estou pensando, entre 0 e 5: "))
computador = randint (0,5)

print("PROCESSANDO ...")
sleep(2)

if jogador == computador:   
    print("Acertou MIZERAVI!")
else:S
    print("ERROU, eu pensei no número {}!".format(computador))ff