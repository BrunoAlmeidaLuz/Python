"""
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.
"""
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = 0
while c < 10:
    if c == 0:
        print('{} -> '.format(termo), end='')
        c = c + 1
    else:
        termo = termo + razao
        print('{} -> '.format(termo), end='')
        c = c + 1
print('Acabou')
