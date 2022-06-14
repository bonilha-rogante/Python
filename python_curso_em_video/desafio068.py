# Programa que jogue par ou ímpar
from random import randint

computador = randint(0, 10)
s = par = impar = 0
escolha = ' '
while escolha not in 'PI':
    escolha = input('Par ou Ímpar [P/I]: ').strip().upper()[0]
while True:
    n = int(input('Digite o número: '))
    s = n + computador
    if escolha == 'P':
        if s % 2 == 0:
            print('Você Venceu')
        else:
            print('Você Perdeu')
            break
    if escolha == 'I':
        if s % 1 == 0:
            print('Você Venceu')
        else:
            print('Você Perdeu')
            break
print(f'Você jogou {n} e o PC {computador}, a soma é {s}')
