# leia  o sexo de uma pessoa, mas só aceite M ou F


print('=====Desafio 057=====')
sexo = input('Digite seu sexo [M/F]: ').strip().upper()
while sexo not in 'MF':
    print('Inválido! Digite novamente.')
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()
print('FIM')


'''
sexo = input('Informa seu sexo[M/F]: ').strip().upper()[0]

while sexo not in 'MF':
    sexo = input('Informação inválida! Por favor, digite novamente: ').strip().upper()[
        0]
print(f'Sexo {sexo} registrado.')'''


'''
sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input(
        'Dados inválidos! Por favor, informe seu sexo: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
'''
