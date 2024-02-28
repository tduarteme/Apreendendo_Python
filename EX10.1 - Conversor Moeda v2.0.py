"""Este programa, faz calculo de quanto custará um produto na cotação atual."""

print("="*77)
print(" Olá Brasileiro, para saber o custo do produto/serviço estrangeiro, convertido em Real. \n Siga os passos a seguir:")
print("="*77)
cotação_atual = float(input(" Informe a cotação atual da moeda desejada: "))
produto_serviço = float(input(" Valor do produto/serviço: "))

print (" Certo, o valor convertido é de R${:.2f}" .format(cotação_atual*produto_serviço))