"""
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
os espaços. Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA.
"""
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# inverso = junto[::-1] <- Metodo de fatiamento
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('A frase {} invertida é {}.'.format(junto, inverso))
if junto == inverso:
    print('Essa frase É UM PALÍNDROMO!')
else:
    print('Essa frase NÃO É UM PALÍNDROMO!')
