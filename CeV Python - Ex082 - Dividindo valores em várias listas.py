"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
mostre o conteúdo das três listas geradas.
"""
lista = []
listaPar = []
listaImpar = []
continuar = 'S'
posicao = 0
while True:
    if continuar == 'S':
        n = int(input('Digite um valor: '))
        lista.append(n)
        continuar = input('Deseja continuar? [S/N]: ').upper()
        if continuar not in 'SN':
            continuar = input('Opção inválida. Deseja continuar? [S/N]: ').upper()
    else:
        break
while posicao < len(lista):
    if lista[posicao] % 2 == 0:
        listaPar.append(lista[posicao])
        posicao += 1
    else:
        listaImpar.append(lista[posicao])
        posicao += 1
print('=-' * 30)
print(f'Os valores da lista original são {lista}.')
print(f'Os valores pares são {listaPar}.')
print(f'Os valores ímpares são {listaImpar}.')
