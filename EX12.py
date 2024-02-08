"""Desenvolva uma solução, que leia o valor do produto e conceda o desconto de 5%."""

produto = float(input("Digite o valor do Produto: "))
valor_promo = (produto - (produto*5)/100)

print(" Tenho uma surpresa para você, este produto custava {:.2f}R$. \n Você ganhou 5% desconto, agora valerá {:.2f}R$" .format(produto, valor_promo))