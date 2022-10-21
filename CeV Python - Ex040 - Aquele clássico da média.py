"""
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
"""
print('=*=' * 15)
print('SISTEMA DE NOTAS ESCOLARES')
print('=*=' * 15)
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('O aluno está REPROVADO! Sua média foi de {:.1f}.'.format(media))
elif media >= 5 and media <= 6.9:
    print('O aluno está em RECUPERAÇÃO! Sua média foi de {:.1f}'.format(media))
else:
    print('O aluno está APROVADO! Sua média foi de {:.1f}'.format(media))
