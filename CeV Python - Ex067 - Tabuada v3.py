"""
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
print('=*=' * 20)
print('PROGRAMA DE TABUADAS')
print('*Digite um número negativo para sair do programa.')
print('=*=' * 20)
while True:
    print('=*=' * 20)
    num = int(input('Quer ver a tabuada de qual número?: '))
    print('=*=' * 20)
    if num < 0:
        break
    for c in range(1, 11):
        result = num * c
        print(f"{num} X {c} = {result}")
        c += 1
print('PROGRAMA FINALIZADO!')
