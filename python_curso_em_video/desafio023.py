# leia um número de 0 a 9999 e mostre cada um dos digitos separados.

print('=====Desafio 023=====')

numero = int(input('Digite um número: '))


unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(
    f'O número digitado foi,{numero}\nUnidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')
