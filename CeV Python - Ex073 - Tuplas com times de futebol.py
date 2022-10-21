"""
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Avaí.
"""
campeonato = ('Palmeiras', 'Corinthians', 'Fluminense', 'Atletico-PR', 'Flamengo', 'Internacional', 'Atletico-MG',
              'Bragantino', 'Santos', 'America-MG', 'São Paulo', 'Botafogo', 'Goias', 'Ceara', 'Coritiba', 'Avai',
              'Fortaleza', 'Cuiaba', 'Atletico-GO', 'Juventude')
print('==' * 25)
print('{:^46}'.format('BRASILEIRÃO 2022'))
print('==' * 25)
print(f'Os 5 primeiros times do campeonato são: {campeonato[0:5]}')
print(f'Os 4 últimos colocados do campeonato são: {campeonato[-4:]}')
print(sorted(campeonato))
print(f'O time do Avaí está na {campeonato.index("Avai") + 1}ª colocação.')
