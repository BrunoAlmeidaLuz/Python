"""
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
print('==' * 25)
print('             \033[31mJOGO DO PAR OU IMPAR\033[m')
print('==' * 25)
vitoria = 0
while True:
    num = int(input('Escolha um número que irá colocar: '))
    escolha = str(input('Agora escolha se quer Par ou Ímpar [P/I]: ')).strip().upper().split()[0]
    while escolha not in 'PI':
        escolha = str(input('Parâmetro incorreto! Escolha se quer Par ou Ímpar [P/I]: ')).strip().upper().split()[0]
    print('==' * 25)
    pc = randint(0, 100)
    soma = num + pc
    print(f'Você: {num} / PC: {pc}')
    print('==' * 25)
    if soma % 2 == 0:
        if escolha == 'P':
            print(f'Parabéns! O número {soma} é PAR e você VENCEU!')
            vitoria += 1
            print('==' * 25)
        else:
            print(f'Que pena! O número {soma} é PAR e você PERDEU!')
            break
    else:
        if escolha == 'I':
            print(f'Parabéns! O número {soma} é IMPAR e você VENCEU!')
            vitoria += 1
            print('==' * 25)
        else:
            print(f'Que pena! O número {soma} é IMPAR e você PERDEU!')
            break
print('==' * 25)
print(f'Você conseguiu ganhar {vitoria} vezes consecutivas!')
