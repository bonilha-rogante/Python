# refaca o desafio 51. leia um número mostra os 10 primeiros da PA

print('=====Desafio 061=====')


i = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = i + (10 - 1) * r

pos = 0

while pos < decimo:
    pa = r * i + 1
    print(pa)
print('Fim')
