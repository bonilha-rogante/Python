# leia vários números inteiros e só pare quando digitar 999, ao final mostre qutos foram digitados e qual a soma desconsiderando o flag

print('=====Desafio 064=====')


n = 0
total = 0
soma = 0
while n != 999:
    n = int(input('Digite um número: '))

    total += 1
    soma += n
print(
    f'O total de número que você digitou foi {total} e a soma entre eles é de {soma}')
