# leia um ano e veja se é bissexto
from datetime import date

print('=====Desafio 032=====')

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual. '))

ano_bis = (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0)

if ano == 0:
    ano = date.today().year
if(ano_bis == True):
    print(f'Você escolheu o ano {ano} e ele É Bissexto.')
else:
    print(f'Você escolheu o ano {ano} e ele NÃO é Bissexto')
