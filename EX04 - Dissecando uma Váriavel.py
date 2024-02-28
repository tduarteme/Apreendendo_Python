"""Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo, 
se possível também, apresente todas as informações sobre ele."""

v= input ("Digite algo: ")

print ("O valor digitado {}, seu tipo primitivo é {} " .format (v, type(v)))
print ("{}, possuí espaços? {} " .format(v, v.isspace()))
print ("{} é númerico? {}".format(v, v.isnumeric()))
print ("{} é Alfabético? {}" .format(v, v.isalpha()))
print ("{} é Alfanumérico? {} ".format(v, v.isalnum()))
print ("{} está maiúsculo? {}".format(v, v.isupper()))
print ("{} está minúscula? {}".format(v, v.islower()))
print ("{} está capitalizada? {}".format(v, v.istitle()))






