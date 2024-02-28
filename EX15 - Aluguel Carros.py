"""Desenvolva uma solução, que pergunte a quantidade de Km percorridos e a quantidade de dias, por um carro alugado.
Calcule o custo, sabendo que a diária é de R$60 e R$0,15 por km rodado."""

dia = int(input(" Pretente alugar por quantos dias?  "))
km = float(input(" km rodados: "))

diaria = (dia * 60) + (km * 0.15)

print("O custo ficará em R${:.2f}" .format(diaria))