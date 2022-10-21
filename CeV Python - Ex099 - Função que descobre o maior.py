"""
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep


def maior(numeros):
    print('Analisando os valores passados...', flush=True)
    sleep(1)
    print(f'Foram informados os valores {numeros}, totalizando {len(numeros)} números.')
    print(f'O maior valor informado foi {max(numeros)} ')


num = []
while True:
    num.append(int(input('Número: ')))
    cont = input('Deseja continuar? [S/N]: ').upper()[0]
    if cont == 'N':
        break
    while cont not in 'SN':
        cont = input('Opção inválida! Digite S ou N: ').upper()[0]
print('=-' * 20)
maior(num)
