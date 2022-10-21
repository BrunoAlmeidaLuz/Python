# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. # Calcule o preço a pagar, sabendo que o carro custa
# R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos quilometros foram percorridos pelo carro?: '))
dias = float(input('Por quantos dias ele foi alugado?: '))
valordia = dias*60
valorkm = km*0.15
print('O valor das diárias foi de R${:.2f}, dos Km foi de R${:.2f}, totalizando R${:.2f}'.format(valordia, valorkm, (valorkm+valordia)))
