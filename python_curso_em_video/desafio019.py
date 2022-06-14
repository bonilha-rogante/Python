# Prof vai sortear 1 dos 4 alunos. Leia os nomes e escolha
from random import choice
print('=====Desafio 019=====')

a1 = input('Digite o nome do Primeiro aluno: ')
a2 = input('Digite o nome do Segundo aluno: ')
a3 = input('Digite o nome do Terceiro aluno: ')
a4 = input('Digite o nome do Quarto aluno: ')

alunos = [a1, a2, a3, a4]
escolhido = choice(alunos)
print(f'O aluno escolhido foi {escolhido}.')
