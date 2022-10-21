"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi
o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = []
maior = 0
menor = 0
posicaomaior = 0
posicaomenor = 0
for n in range(0, 5):
    lista.append(int(input(f'Digite o valor para a posição {n}: ')))
    if n == 0:
        maior = lista[n]
        menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
            menor = lista[n]
print("=-" * 30)
print(f'Você digitou os valores {lista}!')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()
