# Leia o número e mostra a tabuada

print('=====Desafio 09=====')

n = int(input('Digite o número que deseja fazer a tabuada: '))

for c in range(0, 11):
    tab = n * c
    print(f'A tabulado do {n} é: ')
    print(f' {n} X {c} = {tab}')


'''
n = int(input('Digite um número: '))

print(f'A tabuada do {n} é:')
for c in range(1, 11):
    r = n * c
    print(f'{n} X {c} = {r}')'''
