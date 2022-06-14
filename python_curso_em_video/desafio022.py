# Leia Nome completo - Mostre Maiúscula - Minúsccula - Quantas Letras sem cosniderar espaços - Quantas letras #tem o primeiro nome

print('=====Desafio 022=====')

nome = input('Digite seu nome completo: ').strip()

up = nome.upper()
down = nome.lower()
letras = len(nome) - nome.count(' ')
letra_primeiro_nome = nome.split()  # nome.find(' ')

print(
    f'Seu nome completo é {nome}, \nEle em letras Maiúsculas é {up},\nEm letras minúsculas {down}\nA quantidade de letra é {letras}\nE a quantidade de letras no primeiro nome é de {len(letra_primeiro_nome[0])}')
