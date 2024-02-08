"""Escreva uma programa que receba um valor em metros, converte-o em centímetros e milímetros."""

m = float (input ("Digite um valor em METROS: "))

print ("{} dm" .format(m * 10))
print ("{}cm".format(m * 100))
print ("{}mm " .format(m * 1000))

print("="*70)

# Resolvi acrescentar mais unidades, para enriquecer o aprendizado.

print ("{}dam" .format (m / 10))
print ("{}hm" .format(m / 100))
print ("{}km" .format(m / 1000))

