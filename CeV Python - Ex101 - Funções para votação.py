"""
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
nas eleições.
"""


def voto(nasc):
    from datetime import date
    valid = ''
    anoatual = date.today().year
    idade = anoatual - nasc
    if idade < 16:
        valid = f'Você tem {idade} anos - Você NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        valid = f'Você tem {idade} anos - Seu voto é OPCIONAL'
    else:
        valid = f'Você tem {idade} anos - Seu voto é OBRIGATÓRIO'
    return valid


print('=-' * 30)
print(f'{"VERIFICADOR DE SITUAÇÃO ELEITORAL":^60}')
print('=-' * 30)
nascimento = int(input('Digite o seu ano de nascimento: '))
print(f'Situação do voto: {voto(nascimento)}')
