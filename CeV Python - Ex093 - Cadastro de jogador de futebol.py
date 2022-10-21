"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
estatistica = {'Nome': input('Nome do Jogador: ').title()}
gols = []
total = 0
partidas = int(input(f'Quantas partidas {estatistica["Nome"]} jogou?: '))
for c in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na partida {c}?: ')))
    total += gols[c-1]
    estatistica['Gols'] = gols
estatistica['Total de Gols'] = total
print('=-' * 30)
print(estatistica)
print('=-' * 30)
for k, v in estatistica.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {estatistica["Nome"]} jogou {partidas} partidas.')
for c in range(1, partidas + 1):
    print(f'=> Na partida {c}, fez {gols[c-1]} gols.')
print(f' Foi um total de {estatistica["Total de Gols"]} gols.')
