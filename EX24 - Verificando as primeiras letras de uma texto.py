"""Crie um programa que leia o nome de uma cidade, 
diga se começa ou não com o nome (SANTO)"""

cidade = str(input("Informe sua cidade Natal: ")).strip()

print(cidade[:5].lower() =="santo")
