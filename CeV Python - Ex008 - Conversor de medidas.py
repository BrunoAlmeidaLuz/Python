# Exercício Python 8: Escreva um programa que leia um valor em metros e o
# exiba convertido em centímetros e milímetros.

metros = float(input('Digite um valor em metros: '))
print('Esse valor são {} centímetros'.format(metros*100))
print('Esse valor são {} milímetros'.format(metros*1000))
