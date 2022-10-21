"""
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
"""
print('=*=' * 15)
print('COMPARAÇÃO DE VALORES')
print('=*=' * 15)
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print('O primeiro valor {} é maior que o segundo valor {}'.format(num1, num2))
elif num1 < num2:
    print('O segundo valor {} é maior que o primeiro valor {}'.format(num2,num1))
else:
    print('Os valores {} e {} são iguais!'.format(num1, num2))
