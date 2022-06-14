# Um programa que leia vários números inteiros. Para quando digitar 999 e soma todos os números

print('=====Desafio 066=====')
s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} números e a soma é {s}')
'''s = c = 0
while True:
    n = int(input('DIgite um número (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A quantidade de números foi {c} e a soma deles foi {s}')'''
