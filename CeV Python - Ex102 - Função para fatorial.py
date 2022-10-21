"""
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não
na tela o processo de cálculo do fatorial.
"""


def linha():
    print('=-' * 30)

def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


linha()
print(f'{"CALCULO DE FATORIAL":^57}')
linha()
numero = int(input('Insira um numero: '))
mostrar = input('Deseja mostrar o fatorial? [S/N]: ').upper()[0]
linha()
while mostrar not in 'SN':
    mostrar = input('Entrada inválida. Escolha S ou N: ').upper()[0]
if mostrar in 'S':
    print(fatorial(numero, True))
else:
    print(fatorial(numero))
