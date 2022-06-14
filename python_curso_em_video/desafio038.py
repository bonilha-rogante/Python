# Leia 2 números e mostre, o primeiro valor é maior, o segundo valor é maior, os 2 são iguais
print('=====Desafio 038=====')


n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print(f'O primeiro número que foi {n1} é maior que o segundo que foi {n2}')
elif n1 < n2:
    print(f'O segundo número que foi {n2} é maior que o primeiro que foi {n1}')
else:
    print(f'Os número {n1} e {n2} são iguais.')
