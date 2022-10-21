"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""
from datetime import date
print('=*=' * 15)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('=*=' * 15)
nasc = int(input('Digite o ano de nascimento do atleta: '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: MIRIM.')
elif idade <= 14:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: INFANTIL.')
elif idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: JUNIOR.')
elif idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: SENIOR.')
else:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: MASTER.')
