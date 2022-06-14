# cria um programa que leia uma frase qualquer e diga se ela é palíndromo

frase = input('Digite uma frase: ').strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''  # Como se fosse um contador - começa vazio
inverso = junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não é palíndromo')


'''
frase = input('Digite uma frase: ').strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for c in range(len(junto) - 1, -1, -1):
    inverso += c
    print(c)'''


'''
frase = input('Digite uma frase: ').strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
#inverso = ''
inverso = junto[::-1]
'''

'''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
'''
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print(f'Temos um Palíndromo')
else:
    print(f'Não temos um Palíndromo')
'''
