"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
print('==' * 25)
print('                   \033[31mSUPAMAKETO\033[m')
print('==' * 25)
quantProd = menor = c = total = 0
nome = ''
while True:
    produto = str(input('Insira o nome do produto: ')).strip().title()
    preco = float(input('Insira o valor do produto: '))
    total += preco
    c += 1
    if c == 1 or preco < menor:
        menor = preco
        nome = produto
    if preco > 1000:
        quantProd += 1
    continua = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
print(f'O total da sua compra foi de R${total:.2f} em {c} produtos.')
print(f'{quantProd} produtos custam mais de R$1000.')
print(f'O produto mais barato é {nome}.')
