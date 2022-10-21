# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de
# desconto.

produto = float(input('Insira o preço do produto: R$'))
print('O preço do produto com 5% de desconto é: R${:.2f}'.format(produto-(produto*0.05)))
