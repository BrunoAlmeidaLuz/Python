"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
pessoas = []
dados = []
continua = 'S'
mai = men = 0
separador = ('=-' * 35)
print(separador)
while True:
    if continua == 'S':
        dados.append(str(input('Nome: ').upper()))
        dados.append(float(input('Peso: ')))
        if len(pessoas) == 0:
            mai = men = dados[1]
        else:
            if dados[1] > mai:
                mai = dados[1]
            if dados[1] < men:
                men = dados[1]
        pessoas.append(dados[:])
        dados.clear()
        continua = input('Deseja continuar? [S/N]: ').upper()
        if continua not in 'SN':
            continua = input('Opção Inválida. Deseja continuar? [S/N]: ').upper()
    else:
        break
print(separador)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
