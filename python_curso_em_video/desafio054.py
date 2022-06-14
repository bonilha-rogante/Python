# crie um programa que leia o ano de nascimento de sete pessoas e mostre quantas ainda não atingiram a maioridade

from datetime import date

atual = date.today().year
maior = menor = 0

for c in range(1, 8):
    ano = int(input(f'Digite o ano da {c}ª primeira pessoas: '))
    idade = atual - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print(f'Das 7 pessoas, {menor} ainda não são maiores e {maior} são maiores')


'''
from datetime import date

atual = date.today().year
maior = 0
menor = 0


for c in range(1, 8):
    ano = int(input(f'O ano de nascimento da {c}ª pessoa: '))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas já atingiram a maioridade')
print(f'{menor} pessoas ainda não atingiram a maioridade')'''


'''
atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade.')
print(f'E também tivemos {totmenor} pessoas menores de idade.')
'''

'''
atual = date.today().year

for c in range(0, 7):
    p = int(input('Digite o ano de nascimento: '))
    idade = atual - p
    maior = idade >= 21
    if maior:
        print(f'Você tem {idade} anos e já completou a maioridade.')
    else:
        print(f'Você tem {idade} anos e ainda não completou a maioridade')
'''
