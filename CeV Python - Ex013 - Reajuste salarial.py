# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.

salario = float(input('Digite o valor do seu salário: R$'))
print('O seu salário com 15% de aumento será de R${:.2f}'.format(salario+(salario*0.15)))
