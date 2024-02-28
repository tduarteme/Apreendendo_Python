"""Crie um programa que leia o nome completo da pessoa, e informe se contém (SILVA)"""
nome = str(input("informe seu Nome Completo: ")).strip()
print("Seu nome tem Silva? {}".format("silva" in nome.lower()))