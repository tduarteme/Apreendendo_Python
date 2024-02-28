""" O professor do exercíco anterior, quer sortear a ordem de apresentação dos trabalhos.
Desenvolva uma solução que leia quatro alunos e mostre a ordem dos mesmos"""

from random import shuffle
aluno1 = str (input("Nome do primeiro Estudante: "))
aluno2 = str (input("Nome do segundo: "))
aluno3 = str (input("Nome do terceiro: "))
aluno4 = str (input("Nome do Quarto: "))

escolhido = [aluno1, aluno2, aluno3, aluno4]
shuffle(escolhido)

print ("A ordem de apresentação ficou dessa maneira, {}".format(escolhido))