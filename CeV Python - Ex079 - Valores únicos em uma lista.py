"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
"""
num = []
validador = 0
continuar = 'S'
while continuar != 'N':
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = input('Deseja continuar? [S/N]: ').upper()
    if continuar not in 'SN':
        continuar = input('Opção inválida. Deseja continuar? [S/N]: ').upper()
print('=-' * 35)
print(f'A lista de valores digitados em ordem crescente é: {sorted(num)}')
