# leia o comprimento do cateto oposto e do cateto adjacente de um triangulo. Calcule ahipotenusa

from math import hypot
print('=====Desagio 017=====')

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hip = hypot(co, ca)

print(f'A hipotenusa vai medir {hip :.2f}')


#co = float(input('Digite o valor do cateto oposto: '))
#ca = float(input('Digite o valor do cateto adjacente: '))

#hip = (co**2) + (ca**2) ** (1/2)

#print(f'O valor da hipotenusa é de {hip :.2f}')
