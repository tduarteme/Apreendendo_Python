"""Desenvolva a solução abaixo: 
  Quantas vezes a letra A aparece
  Sua primeira e última posição"""

frase = str(input("Digite uma frase: ")).strip().lower()
print("A letra A aparece {} vezes".format(frase.lower().count("a")))
print("A primeira letra A surgiu na posição {}".format(frase.find("a")+1))
print("A última letra A surgiu na posição {}".format(frase.rfind("a")+1))