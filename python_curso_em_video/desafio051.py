# leia primeiro termo e a razão aritimética PA e mostre os 10 primeiros termos dessa progressão


print('=====Desafio 051=====')

i = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
decimo = i + (10 - 1) * r  # formula para encontrar o termo desejado na P.A

for c in range(i, decimo + r, r):
    print(c)
print('Fim')


'''
i = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = i + (10 - 1) * r
for c in range(i, decimo + r, r):
    print(c)'''


'''
i = int(input('Digite o primeiro termo da prograssão que você quer ver: '))
r = int(input('Digite a razão da sua PA: '))
decimo = i + (10 - 1) * r
for c in range(i, decimo + r, r):
    print(f'{c}')
'''
