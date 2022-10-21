"""
Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""
nome = str(input('Digite seu nome: ')).upper().strip().split()
print('Seu nome tem Silva? {}'.format('SILVA' in nome))
