# crie uma tabuada com for

from time import sleep
print('=====Desafio 049=====')
n = int(input('Digite um número: '))
f = int(input('Até onde você quer a tabuada? '))
tab = 0
for c in range(0, f + 1):
    tab = c * n
    sleep(1)
    print(f'{n} X {c} = {tab}')
print('FIM')


'''n = int(input('Digite o número: '))
print(f'A tabuada do {n} é\n')
for c in range(1, 11):
    r = n * c
    print(f'{n} X {c} = {r}')'''


'''
n = int(input('Digite um número: '))
print(f'A tabuada do {n} é:\n ')

for c in range(1, 11):
    r = n * c
    print(f'{n} X {c} = {r}')
'''

'''
for i in range(0, 10):
    i += 1
    t = n * i
    print(f'{n} x {i} = {t}')
'''
