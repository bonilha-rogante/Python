# soma entre todos os número ímpares que são múltiplicados por 3 e que se encontram no intervalo de 1 até 500
s = cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print(f'São {cont} número ímpares e a soma é {s}')


'''print('=====Desafio 048=====')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'São {cont} número ímpares e a soma é de {soma}')'''


'''
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print(f'A soma dos {cont} números ímpares é {s}')
'''
