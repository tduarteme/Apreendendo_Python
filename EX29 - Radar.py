"""Crie uma solução que leia a velocidade de um carro, se ultrapassar 80km/h, alerte-o que foi multado,
o custo será de R$7,00 por cada KM excedido do limite."""

from time import sleep
velocidade = float(input("Velocidade atual do veículo: "))
multa = (velocidade - 80) * 7
print("Por favor aguarde, estamos processando ...")
sleep(5)
if velocidade > 80:
    print("Você ultrapassou o limite de 80km/h e foi multado em R${:.2f}, Respeite as leis de trãnsito!".format(multa))
else:
    print("Parabéns, você é um exemplo de motorista a ser seguido!")