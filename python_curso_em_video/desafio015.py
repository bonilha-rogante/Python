# Pergunte  a quantidade de KM percorridos por um carro alugado e a quantidade de dias
# O valor do carro é 60 por dia  e 0.15 por km

print('=====Desafio 015=====')

km = float(input('Digite a quantidade de Kilometros que você rodou com o carro: '))
dias = int(input('Digite quantos dias você ficou com o carro: '))

total = km * 0.15 + 60 * dias
print(
    f'Você rodou {km:.2f}Km em {dias} dias\nO valor total ficou em R${total:.2f}')


'''
dias = int(input('Você ficou com o carro por quantos dias?  '))
km = float(input('Você percorreu quantos Kilometros: '))

aluguel = (dias * 60) + (km * 0.15)

print(f'Você ficou {dias} dias com o carro e \npercorreu {km}Km.\nSendo assim, o total a pargar é de R${aluguel :.2f}.')
'''
