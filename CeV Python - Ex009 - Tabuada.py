# Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Insira um número: '))
n1 = 1
while n1 < 11:
    r = (n*n1)
    print('{} X {} = {}'.format(n, n1, r))
    n1 = n1+1
