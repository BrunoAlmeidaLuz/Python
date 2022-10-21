"""
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
maior = 0
menor = 0
media = 0
nomemaior = ''
quanthomem = 0
quantmulher = 0
print('=*=' * 20)
print('\033[31mANALISADOR COMPLETO\033[m')
print('=*=' * 20)
for p in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(p))).strip().title()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(p)))
    sexo = str(input('Digite o sexo (M/F) da {}ª pessoa: '.format(p)))
    media += idade
    if sexo == 'M' or sexo == 'm':
        if idade > maior:
            maior = idade
            nomemaior = nome
            quanthomem = quanthomem + 1
    if sexo == 'F' or sexo == 'f':
        if idade < 20:
            menor = menor + 1
            quantmulher = quantmulher + 1
print('=*=' * 20)
print('A média de idade do grupo é de {} anos.'.format(media / 4))
if quantmulher != 0:
    print('Nesse grupo tem {} mulheres com menos de 20 anos.'.format(menor))
if quanthomem == 0:
    print('Não existem homens nessa lista.')
else:
    print('O homem mais velho tem {} anos e se chama {}.'.format(maior, nomemaior))
