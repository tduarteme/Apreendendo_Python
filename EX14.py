"""Resolva este problema, faça a conversão de C° para F° e apresente os valores na tela."""

c = float(input(" Temperatura em C°: "))

print("A temperatura de {}C°, equivale a {:.1f}F° " .format(c, (c * 1.8)+32))

print("="*70)

print("Em Kelvin, equivale a {:.2f}K° " .format(c + 273.15))

print("="*70)