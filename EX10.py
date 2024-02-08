"""Desenvolva uma solução que leia quanto dinheiro a pessoa têm, e mostre quantos Dólares ela pode comprar.
US$1 == R$3.27"""

dinheiro = float(input("Digite o valor em R$: "))
dolar = dinheiro/3.27

print("Com R$ {}, você consegue comprar US$ {:.2f}" .format(dinheiro, dolar))