# Exercicio 018 - Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e
# tangente desse angulo
import math
angulo = float(input('Insira o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O valor do Seno é {:.2f}, do Cosseno é {:.2f} e da Tangente é {:.2f}'.format(seno, cosseno, tangente))
