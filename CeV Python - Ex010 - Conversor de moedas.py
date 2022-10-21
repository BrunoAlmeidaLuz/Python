# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos dólares ela pode comprar

#Dolar 5.30

dolar = float(5.30)
carteira = float(input('Quantos reais você tem na carteira?: R$'))
print('Com isso, meu amigo, você consegue comprar U${:.2f} dólares'.format(carteira/dolar))
