# Exercicio 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
alunoa = input('Digite o nome do primeiro aluno: ')
alunob = input('Digite o nome do segundo aluno: ')
alunoc = input('Digite o nome do terceiro aluno: ')
alunod = input('Digite o nome do quarto aluno: ')
lista = [alunoa, alunob, alunoc, alunod]
print('O aluno escolhido para apagar o quadro será: {}'.format(choice(lista)))
