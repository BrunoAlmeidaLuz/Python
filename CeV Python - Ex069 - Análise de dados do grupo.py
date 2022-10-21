"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""
print('==' * 25)
print('                \033[31mPROGRAMA DE CADASTRO\033[m')
print('==' * 25)
maior = 0
homem = 0
mulher = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper().split()[0]
    while sexo not in 'MF':
        sexo = str(input('Parâmetro incorreto. Digite o sexo [M/F]: ')).strip().upper().split()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher += 1
    escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper().split()[0]
    if escolha == 'N':
        break
print('==' * 25)
print(f'Foram cadastradas {maior} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homem} homens.')
print(f'Foram cadastradas {mulher} mulheres com menos de 20 anos.')
