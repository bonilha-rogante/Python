# leia 3 segmentos de reta e vertifique se formam um triângulo. se formar 1-equilátero, 2, isósceles, 3- escaleno

print('=====Desafio 042=====')

l1 = float(input('Digite o tamanho da primeira reta: '))
l2 = float(input('Digite o tamanho da segunda reta: '))
l3 = float(input('Digite o tamanho da terceira reta: '))

triangulo = l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2
equi = l1 == l2 == l3
esca = l1 != l2 != l3 != l1
if triangulo:
    print(
        f'Suas retas são {l1}, {l2} e {l3} e é possível formar um triângulo.')
    if equi:
        print(f'Seu Triângulo é EQUILÁTERO')
    elif esca:
        print(f'Seus Triângulo é ESCALENO')
    else:
        print(f'Seu Triângulo é ISÓSCELES.')
else:
    print(
        f'Suas retas foram {l1}, {l2} e {l3} e não foi possível formar um triângulo.')
