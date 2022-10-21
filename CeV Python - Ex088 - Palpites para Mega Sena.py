"""
Exercício Python 088b Alternativo: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep
lista = []
apostas = []
tot = 1
titulo = 'Gerador de Números para Mega Sena'
print('=-' * 35)
print(f'{titulo:^70}')
print('=-' * 35)
qtdJogos = int(input('Quantos jogos deseja gerar?: '))
print()
print(f'Gerando os {qtdJogos} palpites...Aguarde..')
print()
sleep(1)
while tot <= qtdJogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    apostas.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(apostas):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('=-' * 35)
print('Boa sorte!')
