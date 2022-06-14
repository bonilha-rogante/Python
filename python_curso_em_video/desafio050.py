# lei 6 número inteiros, mostre a soma apenas dos que forem pares.

print('=====Desafio 050=====')
s = cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        cont += 1
        s += n
print(f'Você digitou {cont} número pares e a soma deles foi de {s}')


'''
soma = 0
cont = 0

for c in range(1, 7):
    n = int(input(f'Digite {c}º número: '))

    if n % 2 == 0:
        soma += n
        cont += 1


print(f'Você digitou {cont} números pares e a soma entre eles é de {soma}')'''


'''
s = 0
cont = 0

for c in range(1, 7):
    n = int(input(f'Digite um {c}º número: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Você informou {cont} número pares e a soma dos números é de {s}.')
'''
