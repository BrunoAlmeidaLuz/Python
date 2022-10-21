"""
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
aluno = {'Nome': input('Nome: ').title(), 'Média': float(input('Média: '))}
if aluno['Média'] >= 7:
    aluno['Situação'] = 'aprovado(a)'
else:
    aluno['Situação'] = 'reprovado(a)'
print('=-' * 35)
print(f'O aluno {aluno["Nome"]} teve média {aluno["Média"]} e portanto está {aluno["Situação"]}.')
