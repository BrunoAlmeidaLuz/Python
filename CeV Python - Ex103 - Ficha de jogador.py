"""
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o
nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente.
"""


def ficha(nome='', gols=0):
    if nome == '':
        nome = '<Desconhecido>'
        print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')
    else:
        print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')


jogador = input('Digite o nome do Jogador: ').title()
qtdgols = input(f'Quantos gols {jogador} marcou?: ')
if qtdgols.isnumeric():
    qtdgols = int(qtdgols)
else:
    qtdgols = 0
print('=-' * 30)
ficha(jogador, qtdgols)
