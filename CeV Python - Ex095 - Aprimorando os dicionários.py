"""
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador.
"""
estatistica = {}
jogadores = []
"Pegando dados dos jogadores e cadastrando na lista"
while True:
    estatistica.clear()
    gols = []
    total = 0
    estatistica['Nome'] = input('Nome do Jogador: ').title()
    partidas = int(input(f'Quantas partidas {estatistica["Nome"]} jogou?: '))
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na partida {c}?: ')))
        total += gols[c-1]
        estatistica['Gols'] = gols
    estatistica['Total de Gols'] = total
    jogadores.append(estatistica.copy())
    continua = input('Deseja continuar? [S/N]: ').upper()[0]
    while continua not in 'SN':
        continua = input('Opção inválida! Digite S ou N: ').upper()[0]
    if continua == 'N':
        break
"Imprimindo a tabela de estatísticas na tela"
print('=-' * 30)
print('cod ', end='')
for i in estatistica.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-' * 30)
"Verificando os detalhes de cada jogador"
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[busca]["Nome"]} --')
        for i, g in enumerate(jogadores[busca]["Gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('=-' * 30)
print('<<< VOLTE SEMPRE >>>')
