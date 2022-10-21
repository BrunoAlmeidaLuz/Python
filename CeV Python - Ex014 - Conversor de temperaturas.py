# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e
# converta para graus Fahrenheit.

temp = float(input('Digite a temperatura em ºC: '))
print('A temperatura {:.1f}ºC equivale à {:.1f}ºF'.format(temp, ((temp*1.8)+32)))
