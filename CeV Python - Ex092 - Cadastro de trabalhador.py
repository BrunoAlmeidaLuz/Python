"""
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date
from time import sleep
anoAtual = date.today().year
cadastro = {}
while True:
    print('=-' * 30)
    cadastro['Nome'] = input('Nome: ').title()
    cadastro['Idade'] = anoAtual - (int(input('Ano de Nascimento: ')))
    carteira = int(input('CTPS (0 não tem): '))
    if carteira != 0:
        cadastro['CTPS'] = carteira
        cadastro['Ano de Contratação'] = int(input('Ano de contratação: '))
        cadastro['Salário'] = float(input('Salário: '))
        aposenta = cadastro['Idade'] + ((cadastro['Ano de Contratação'] + 35) - date.today().year)
        cadastro['Aposentadoria'] = aposenta
        break
    else:
        cadastro['CTPS'] = carteira
        break
print('=-' * 30)
sleep(1)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
    sleep(1)
print('=-' * 30)
print('<<<<FIM DA ANÁLISE>>>>')
