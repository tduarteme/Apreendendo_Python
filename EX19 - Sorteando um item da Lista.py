"""O professor quer sortear quatro alunos para apagar o quadro. Faça um programa que leia e escolha em entre eles"""
import random
# from import import choice -> Outra maneira de importar a biblioteca

aluno1 = str(input("Digite o nome do primeiro Aluno: "))
aluno2 = str(input("Digite o nome do segundo Aluno: "))
aluno3 = str(input("Digite o nome do terceiro Aluno: "))
aluno4 = str(input("Digite o nome do quarto Aluno: "))

sorteio = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(sorteio)

print("O aluno sorteado foi {}".format(escolhido))