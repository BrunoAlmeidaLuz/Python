"""
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
"""


def area(a, b):
    print(f'A área de um terreno {a} x {b} é de {a * b}m².')


print('CONTROLE DE TERRENOS')
print('-' * 30)
lg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(lg, comp)
