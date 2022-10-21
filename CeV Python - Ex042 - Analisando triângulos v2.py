"""
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
formado:

– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
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
            if n1 == n2 == n3:
                print('Os segmentos acima podem formar um triângulo EQUILÁTERO.')
            elif n1 != n2 != n3 != n1:
                print('Os segmentos acima podem formar um triângulo ESCALENO.')
            else:
                print('Os segmentos acima podem formar um triângulo ISÓSCELES.')
        else:
            print('Não é possível formar um triângulo com os segmentos acima!')
    else:
        print('Não é possível formar um triângulo com os segmentos acima!')
else:
    print('Não é possível formar um triângulo com os segmentos acima!')
