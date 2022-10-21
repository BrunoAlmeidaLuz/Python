"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
num1 = float(input('Digite o primeiro valor: '))
print('==' * 20)
num2 = float(input('Digite o segundo valor: '))
print('==' * 20)
soma = 0
multi = 0
opcao = int(input("""
Opções:
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa

Escolha sua opção: """))
while opcao != 5:
    if opcao == 1:
        soma = num1 + num2
        print('==' * 20)
        print('A soma dos dois números é {}.'.format(soma))
        print('==' * 20)
        opcao = int(input('Escolha uma opção: '))
    if opcao == 2:
        multi = num1 * num2
        print('==' * 20)
        print('A multiplicação dos dois números é {}.'.format(multi))
        print('==' * 20)
        opcao = int(input('Escolha uma opção: '))
    if opcao == 3:
        if num1 > num2:
            print('==' * 20)
            print('O maior número é {}.'.format(num1))
            print('==' * 20)
            opcao = int(input('Escolha uma opção: '))
        else:
            print('==' * 20)
            print('O maior número é {}'.format(num2))
            print('==' * 20)
            opcao = int(input('Escolha uma opção: '))
    if opcao == 4:
        print('==' * 20)
        num1 = float(input('Digite o primeiro valor: '))
        print('==' * 20)
        num2 = float(input('Digite o segundo valor: '))
        print('==' * 20)
        opcao = int(input('Escolha uma opção: '))
    elif opcao != 5:
        opcao = int(input('Opção inválida. Digite um número válido: '))
print('==' * 20)
print('Programa encerrado.')
