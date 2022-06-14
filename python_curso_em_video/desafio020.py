# leia 4 nomes e sorteie uma ordem
from random import shuffle

print('=====Desafio 020=====')

a1 = input('Digite o nome do Primeiro aluno: ')
a2 = input('Digite o nome do Segundo aluno: ')
a3 = input('Digite o nome do Terceiro aluno: ')
a4 = input('Digite o nome do Quarto aluno: ')

alunos = [a1, a2, a3, a4]
shuffle(alunos)
print(f'A ordem de aprensentação será:\n{alunos}')
