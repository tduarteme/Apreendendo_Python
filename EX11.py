"""Desenvolva um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e quantidade de tinta necessária para pintá-lo, sabendo que cada
litro de tinta, pinta uma área de 2m²"""

largura = float(input("Largura da Parede: "))
altura = float(input("Largura da Parede: "))
area = largura * altura

#tinta = area / 2 -> O Cáculo poderá ser feito assim, ou da forma abaixo;

print ("A parede possui uma dimensão  de {} X {}, a área equivale a {}m²" .format(largura, altura, area))
print ("Para pintar toda a parede, será necessário {}L de Tinta" .format(area/2))