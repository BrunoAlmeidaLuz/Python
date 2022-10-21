"""
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""
continua = True
media = 0
maior = 0
menor = 0
c = 0
while continua:
    num = int(input('Digite um valor: '))
    if c == 0:
        maior = num
        menor = num
        media += num
        c += 1
    else:
        if num > maior:
            maior = num
            media += num
            c += 1
        if num < menor:
            menor = num
            media += num
            c += 1
    continua = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continua == 'S':
        continua = True
    elif continua == 'N':
        continua = False
print('=*=' * 35)
print('O maior valor dessa lista é: {}.'.format(maior))
print('O menor valor dessa lista é: {}.'.format(menor))
print('A media dos valores digitados é: {}.'.format(media / c))
