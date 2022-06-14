# leia um angulo e mostre seno, cossseno e tangente
from math import radians, sin, cos, tan
print('=====Desafio 018=====')

angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno :.2f}')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno :.2f}')
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente :.2f}')
