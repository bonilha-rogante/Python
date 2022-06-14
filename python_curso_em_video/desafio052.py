# leia um número inteiro e diga se é ou não número primo

print('=====Desafio 052=====')
# Número primo só é divisivel por 1 e por ele mesmo
total = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        total += 1
if total == 2:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')
'''
n = int(input('Digite um número: '))
tot = 0

for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
    else:
        print(c)
print(f'O número {n} foi divisível {tot} vezes.')
if tot == 2:
    print('E por isso ele é Primo')
else:
    print('E por isso ele não é primo')'''


'''
n = int(input('Digite um número: '))
tot = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m')
        tot += 1
    else:
        print('\033[31m')
    print(f'{c}')
print(f'\n\033[m0 O número {n} foi divisível {tot} vezes.')
if tot == 2:
    print('E por isso ele é Primo!')
else:
    print('E por isso ele não é Primo!')
'''
