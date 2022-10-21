"""
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import choice
from time import sleep
print('=*=' * 15)
print('JOKENPÔ')
print('=*=' * 15)
lista = ['Pedra', 'Papel', 'Tesoura']
comp = choice(lista)
print('Vamos jogar Jokenpô?')
jogador = int(input('''Escolha uma opção:
[1] - Pedra
[2] - Papel
[3] - Tesoura
Sua escolha: '''))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')
if comp == 'Pedra':
    if jogador == 1:
        print('O computador escolheu {} e você Pedra. Foi um EMPATE!'.format(comp))
    elif jogador == 2:
        print('O computador escolheu {} e você Papel. Você VENCEU!'.format(comp))
    elif jogador == 3:
        print('O computador escolheu {} e você Tesoura. Você PERDEU!'.format(comp))
    else:
        print('Digite uma opção válida!')
elif comp == 'Papel':
    if jogador == 1:
        print('O computador escolheu {} e você Pedra. Você PERDEU!'.format(comp))
    elif jogador == 2:
        print('O computador escolheu {} e você Papel. Foi um EMPATE!'.format(comp))
    elif jogador == 3:
        print('O computador escolheu {} e você Tesoura. Você VENCEU!'.format(comp))
    else:
        print('Digite uma opção válida!')
elif comp == 'Tesoura':
    if jogador == 1:
        print('O computador escolheu {} e você Pedra. Você VENCEU!'.format(comp))
    elif jogador == 2:
        print('O computador escolheu {} e você Papel. Você PERDEU!'.format(comp))
    elif jogador == 3:
        print('O computador escolheu {} e você Tesoura. Foi um EMPATE!'.format(comp))
    else:
        print('Digite uma opção válida!')
