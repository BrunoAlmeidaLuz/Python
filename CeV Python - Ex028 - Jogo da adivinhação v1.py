"""
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu.
"""
from random import randint
from time import sleep
num = randint(0, 5)
print('=*=' * 20)
print('Estou pensando em um número de 0 a 5. Consegue adivinhar?')
print('=*=' * 20)
user = int(input('Em que número estou pensando?: '))
print('PROCESSANDO...')
sleep(2)
if user == num:
    print('Parabéns! Você adivinhou o número {} que eu escolhi!'.format(num))
else:
    print('Que pena! Eu escolhi {} e você foi derrotado!'.format(num))
