"""
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
par = 0
for c in range(1, 7):
    soma = int(input('Digite um valor: '))
    if soma % 2 == 0:
        par = par + soma
print('A soma dos números pares é {}'.format(par))
