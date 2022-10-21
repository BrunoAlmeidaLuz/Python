"""
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""
print('=*=' * 15)
print('SISTEMA DE VENDAS')
print('=*=' * 15)
valor = float(input('Digite o valor do produto: R$'))
pagamento = int(input('''Escolha a forma de pagamento:
[1] - À vista no dinheiro/cheque
[2] - À vista no cartão
[3] - 2x no cartão
[4] - 3x ou mais no cartão
Sua escolha: '''))
if pagamento == 1:
    valor = valor - (valor * 0.10)
    print('Valor final do produto: R${:.2f}'.format(valor))
elif pagamento == 2:
    valor = valor - (valor * 0.05)
    print('Valor final do produto: R${:.2f}'.format(valor))
elif pagamento == 3:
    parcela = 2
    print('Valor final do produto: R${:.2f}'.format(valor))
    print('Sua compra será em {}x de R${:.2f}'.format(parcela, (valor / 2)))
elif pagamento == 4:
    parcela = int(input('Quantas parcelas? '))
    valor = valor + (valor * 0.20)
    print('Valor final do produto: R${:.2f}'.format(valor))
    print('Sua compra será em {}x de R${:.2f}'.format(parcela, (valor / parcela)))
else:
    print('Entrada inválida.')
