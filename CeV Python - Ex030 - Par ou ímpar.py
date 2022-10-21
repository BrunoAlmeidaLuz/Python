"""
Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
num = int(input('Insira um número: '))
if num % 2 == 0:
    print('{} é um número PAR'.format(num))
else:
    print('{} é um número ÍMPAR'.format(num))
