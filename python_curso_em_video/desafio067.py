# Faça um programa que mostre a tabuada de vários números. um de cada vez. Interrompa quando o número for negativo

from time import sleep
print('=====Desafio 067=====')
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    for c in range(1, 11):
        tab = n * c
        print(f'{n} X {c} = {tab}')
        sleep(0.5)

print('Obrigado!')


'''t = c = 0
n = 1
while True:
    n = int(input('Digite o número que deseja ver a tabuada: '))

    if n != int:
        break

    while c <= 10:
        c += 1
        t = n * c
        print(f'{n} X {c} = {t}')'''
