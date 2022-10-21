"""
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint
from time import sleep
numeros = []


def sorteia(num):
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 100)
        num.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somapar(lst):
    pos = 0
    par = 0
    while pos < len(lst):
        if lst[pos] % 2 == 0:
            par += lst[pos]
        pos += 1
    print(f'A soma dos valores pares da lista {lst} é {par}')


sorteia(numeros)
somapar(numeros)
