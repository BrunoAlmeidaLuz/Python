# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua
# área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área
# de 2 metros quadrados.

altura = float(input('Digite a altura da parede (m): '))
largura = float(input('Digite a largura da parede (m): '))
area = float(altura*largura)
print('A sua parede de {} x {} tem área de {:.2f} metros quadrados'.format(altura, largura, area))
print('A quantidade de tinta para pintar essa parede será de {:.2f} litros'.format(area/2))
