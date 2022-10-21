"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que
agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
print('=*=' * 20)
print('JOGO DA ADIVINHAÇÃO')
print('=*=' * 20)
num = randint(0, 10)
vezes = 1
print('Estou pensando em um número entre 0 e 10. Consegue adivinhar?')
user = int(input('Em que número estou pensando: '))
while user != num:
    if user < num:
        user = int(input('MAIS...Tente novamente: '))
        vezes += 1
    else:
        user = int(input('MENOS...Tente novamente: '))
        vezes += 1
print('Parabéns! Você acertou com {} tentativas!'.format(vezes))
