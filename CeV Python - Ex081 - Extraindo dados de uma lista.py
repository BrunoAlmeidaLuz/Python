"""
Exercício Python 081: crie um programa que vai ler vários números e colocar numa lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
continuar = 'S'
while True:
    if continuar == 'S':
        n = int(input('Digite um valor: '))
        lista.append(n)
        continuar = input('Deseja continuar? [S/N]: ').upper()
        if continuar not in 'SN':
            continuar = input('Opção inválida. Deseja continuar? [S/N]: ').upper()
    else:
        break
print('=-' * 30)
print(f'Foram digitados {len(lista)} números nessa lista.')
print(f'A lista digitada decrescente foi {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 existe na lista.')
else:
    print('O valor 5 não existe na lista.')
