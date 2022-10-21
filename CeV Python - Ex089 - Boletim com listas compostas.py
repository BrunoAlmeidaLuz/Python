"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
"""
titulo = 'Sistema de Notas dos Alunos'
titulo2 = 'Boletim Digital'
aluno = []
continuar = 'S'
print('=-' * 35)
print(f'{titulo:^70}')
print('=-' * 35)
while True:
    if continuar not in 'Nn':
        nome = (input('Nome: ')).upper()
        nota1 = (float(input('Nota 1: ')))
        nota2 = (float(input('Nota 2: ')))
        media = ((nota1 + nota2)/2)
        aluno.append([nome, [nota1, nota2], media])
        continuar = input('Deseja continuar? [S/N]: ').upper()
        if continuar not in 'SN':
            continuar = input('Opção Inválida. Deseja continuar? [S/N]: ').upper()
    else:
        break
print('=-' * 35)
print(f'{titulo2:^70}')
print('=-' * 35)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 35)
for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(aluno) - 1:
        print(f'Notas de {aluno[opc][0]} são {aluno[opc][1]}')
print('<<<<<VOLTE SEMPRE >>>>>')
