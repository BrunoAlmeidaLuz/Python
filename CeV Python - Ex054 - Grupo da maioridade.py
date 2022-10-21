"""
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Digite o {}º ano de nascimento: '.format(c)))
    idade = atual - nasc
    if idade > 21:
        maior += 1
    else:
        menor += 1
print('Dessas pessoas, {} já atingiram a maioridade e {} não.'.format(maior, menor))
