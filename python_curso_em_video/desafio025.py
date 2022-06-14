# leia o nome de uma pessoa e diga se ela tem silva no nome


print('=====Desafio 025=====')

nome = input('Digite seu nome completo: ').strip()

print(f"Tem silva? {'silva' in nome.lower()}")
