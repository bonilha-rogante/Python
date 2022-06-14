# leia nome completo mostre primeiro e último nome separado

print('=====Desafio 027=====')

nome = input('Digite seu nome completo: ')

nome = nome.split()

# len(nome)-1
print(f'Seu primeiro nome é {nome[0]} e seu último nome é {nome[-1]}')
