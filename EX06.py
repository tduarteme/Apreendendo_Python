"""Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""

n= int (input ("Digite um valor: "))

print ("O dobro do valor {}, equivale a {}. ".format(n,(n*2)))
print ("O triplo é {}." .format (n*3))
print ("Já a raiz quadrada, é {:.2f}.".format (n**(1/2)))

# É possível calcular  a raiz quadrada, na forma abaixo;

print("="*70) # -> Este comando serve para criar um espaçamento.
print ("A raiz quadrada de {}, é {:.2f}." .format (n, pow(n, (1/2))))
print("="*70)