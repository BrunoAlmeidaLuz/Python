"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor
da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou
então o empréstimo será negado.
"""
print('=*=' * 15)
print('Sistema de Aprovação de Empréstimos')
print('=*=' * 15)
casa = float(input('Digite o valor do imóvel desejado: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
tempo = float(input('Em quantos meses deseja pagar: '))
valormax = salario * 0.30
parcela = casa / tempo
if parcela > valormax:
    print('O empréstimo foi NEGADO por exceder os 30% permitidos!')
    print('O valor da parcela será de R${:.2f} e o limite é de R${:.2f}'.format(parcela, valormax))
else:
    print('O empréstimo foi APROVADO por estar dentro dos 30% permitidos')
    print('O valor da parcela será de R${:.2f} e o limite é de R${:.2f}'.format(parcela, valormax))
