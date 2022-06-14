# 3 retas e se é possível formar um triângulo
print('=====Desafio 035=====')

r1 = float(input('Primeira Reta: '))
r2 = float(input('Segunda Reta: '))
r3 = float(input('Terceira Reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo.')
else:
    print('Não pode formar um triângulo.')
