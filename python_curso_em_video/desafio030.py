# Leia número e mostre se é ímpar ou par

print('=====Desafio 030=====')

numero = int(input('Digite um número: '))
par = numero % 2 == 0


if(par):
    print(f'Você digitou {numero} e esse número é par')
else:
    print(f'Você digitou {numero} e esse número é ímpar')
