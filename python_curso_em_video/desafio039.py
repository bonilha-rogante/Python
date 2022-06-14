# leia ano de nascimento e se ainda vai se alista, hora de alistar ou já passou da hora
from datetime import date
print('=====Desafio 039=====')


atual = date.today().year

ano = int(input('Digite o ano em que você nasceu: '))

idade = atual - ano
menor = idade < 18
alistar = idade == 18

if menor:
    saldo = 18 - idade
    print(
        f'Você tem {idade} anos e ainda faltam {saldo} e ainda não precisa se alistar.')
elif alistar:
    print(f'Você tem {idade} anos e está na hora de se alistar.')
else:
    saldo = idade - 18
    print(
        f'Você tem {idade} e já se passaram {saldo} anos da hora de se alistar.')
