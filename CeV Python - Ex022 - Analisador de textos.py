"""
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
"""
nome = str(input('Insira seu nome: ')).strip()
lista = nome.split()
print('Maiúsculo: {}'.format(nome.upper()))
print('Minúsculo: {}'.format(nome.lower()))
print('Quantas letras sem espaço: {}'.format(len(nome) - nome.count(' ')))
print('Quantas letras no primeiro nome: {}'.format(len(lista[0])))
