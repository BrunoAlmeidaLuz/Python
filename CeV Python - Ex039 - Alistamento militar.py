"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
print('=*=' * 15)
print('VERIFICADOR DE ALISTAMENTO MILITAR')
print('=*=' * 15)
ano = int(input('Insira o ano do seu nascimento: '))
atual = date.today().year
idade = atual - ano
if idade == 18:
    print('Está na hora de servir seu País! Vá se alistar!')
elif idade < 18:
    saldo = 18 - idade
    alist = atual + saldo
    print('Ainda não é a hora de servir seu País!')
    print('Faltam ainda {} ano(s) para você se alistar!'.format(saldo))
    print('Seu alistamento será em {}'.format(alist))
else:
    saldo = idade - 18
    alist = atual - saldo
    print('Já passou da hora de servir seu País!')
    print('Está com seu alistamento {} ano(s) atrasado!'.format(saldo))
    print('Seu alistamento foi em {}'.format(alist))
