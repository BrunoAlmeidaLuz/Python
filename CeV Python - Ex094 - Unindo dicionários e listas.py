"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
pessoas = {}
galera = []
cont = 0
somaIdades = 0
mulher = []
idadeAcima = []
while True:
    pessoas['Nome'] = input('Nome: ').title()
    while True:
        pessoas['Sexo'] = input('Sexo [M/F]: ').upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoas['Idade'] = int(input('Idade: '))
    galera.append(pessoas.copy())
    cont += 1
    somaIdades += pessoas['Idade']
    if pessoas['Sexo'] == 'F':
        mulher.append(pessoas['Nome'])
    continua = input('Deseja continuar? [S/N]: ').upper()[0]
    while continua not in 'SN':
        continua = input('Erro! Por favor, digite apenas S ou N: ').upper()[0]
    if continua == 'N':
        break
print('=-' * 30)
media = somaIdades/cont
print(f'A) Foram cadastradas {cont} pessoas.')
print(f'B) A média de idade entre todos é de {media:.0f} anos.')
print(f'C) As mulheres dessa lista são: {mulher}')
print(f'D) As pessoas com idade acima da média são: ')
for p in galera:
    if p['Idade'] >= media:
        print()
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('=-' * 30)
print('<<ENCERRADO>>')
