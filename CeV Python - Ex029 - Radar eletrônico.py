"""
Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""
from time import sleep
print('=*=' * 20)
print('SISTEMA DE MULTAS DO DETRAN')
print('=*=' * 20)
velocidade = float(input('Insira a velocidade medida do veículo: '))
if velocidade > 80:
    valor = (velocidade - 80) * 7
    print('Calculando...')
    sleep(2)
    print('Veículo acima do limite de velocidade permitido.')
    print('O valor da multa a ser pago é de R${:.2f}'.format(valor))
else:
    print('Calculando...')
    sleep(2)
    print('Veículo dentro do limite de velocidade permitido.')

