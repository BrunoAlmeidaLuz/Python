"""
Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
não formar um triângulo.
"""
print('=*=' * 15)
print('Analisador de Triângulos')
print('=*=' * 15)
n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))
if (n2 - n3) < n1 < (n2 + n3):
    if (n1 - n3) < n2 < (n1 + n3):
        if (n1 - n2) < n3 < (n1 + n2):
            print('É possível formar um triângulo com os segmentos acima!')
        else:
            print('Não é possível formar um triângulo com os segmentos acima!')
    else:
        print('Não é possível formar um triângulo com os segmentos acima!')
else:
    print('Não é possível formar um triângulo com os segmentos acima!')
