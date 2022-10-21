"""
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter
dados = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6), 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}
ranking = []
print('VALORES SORTEADOS')
print('=-' * 35)
for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('=-' * 35)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
