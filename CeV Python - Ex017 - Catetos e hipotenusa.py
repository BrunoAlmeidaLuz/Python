# Exercicio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triangulo.
# Calcule sua hipotenusa
from math import hypot
catadj = float(input('Insira o valor do cateto adjascente: '))
catopo = float(input('Insira o valor do cateto oposto: '))
print('O valor da hipotenusa desse retângulo é {:.2f}'.format(hypot(catopo, catadj)))


