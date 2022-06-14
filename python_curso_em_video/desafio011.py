# Leia a largura e a altura de uma parede em metros e calcule sua área e a quantidade de tinta para pinta-la.
# 1 litro de tinta, pinta 2m²

print('=====Desafio 10=====')

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura
tinta = area / 2

print(f'Sua parede tem {largura} metros de largura, {altura} metros de altura.\nUma área de {area :.2f}m²\n e será necessário {tinta :.2f} litro de tinta para pinta-la')


'''largura = float(input('Digite quantos metros de largura tem a parede: '))
altura = float(input('Digite quantos metros de altura tem a parede: '))

area = largura * altura
litros = area / 2

print(f'A parede tem {largura} metros de largura e {altura} metros de altura.\n Sua Área é de {area} m². \n Será necessário {litros} litros de tinta para pintá-la.')'''
