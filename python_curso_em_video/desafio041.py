# leia o ano de nascimento e coloque em sua categoria correta. até 9 mirim, até 14 infantil, até 19 junior, até 20 senior e acima master.


from datetime import date
print('=====Desafio 041=====')


atual = date.today().year
ano = int(input('Digite o ano que nasceu: '))

idade = atual - ano

mirim = idade <= 9
infantil = idade <= 14
junior = idade <= 19
senior = idade <= 20

if mirim:
    print(f'Você tem {idade} anos e está na categoria MIRIM.')
elif infantil:
    print(f'Você tem {idade} anos e está na categoria INFANTIL.')
elif junior:
    print(f'Você tem {idade} anos e está na categoria JUNIOR.')
elif senior:
    print(f'Você tem {idade} anos e está na categoria SENIOR.')
else:
    print(f'Você tem {idade} anos e está na categoria MASTER.')
