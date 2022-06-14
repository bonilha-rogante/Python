# leia um número e motre seu fatorial


print('=====Desafio 060=====')

n = int(input('Digite um número: '))

while n != 0:
    fatorial = n
    n -= 1
    r = n * fatorial
    print(r)
print('Fim')
