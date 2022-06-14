# leia nome, idade e sexo de 4 pessoas. Mostre a média de idade. O nome do homem mais velho. Qts mulheres tem - 20 e

print('=====Desafio 056=====')

soma_idade = maior_idade = menor = 0
nome_velho = ''
for c in range(1, 5):
    print(f'{c}ª Pessoa:')
    nome = input('Digite o nome: ').strip()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F] ').strip().upper()

    soma_idade += idade
    media = soma_idade / 4

    if c == 1 and sexo == 'M':
        nome_velho = nome
        velho = idade
    else:
        if idade > velho and sexo == 'M':
            nome_velho = nome
            velho = idade

    if sexo == 'F' and idade < 20:
        menor += 1
print(
    f'A media das idades é {media} a idade do homem mais velho é {nome_velho} e tem {menor} mulheres com menor de 20 anos')


'''
soma_idade = 0
mais_velho = 0
nome_velho = ''
for c in range(1, 5):
    print(f'====={c}ª Pessoa=====')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()

    soma_idade += idade
    media_idade = soma_idade / 4
    if c == 1 and sexo in 'Mm':
        mais_velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome
print(media_idade)'''


'''
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
idade_mulher = 0
for c in range(1, 5):
    print(f'-----{c}ª Pessoa-----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo[M/F]: ').strip()
    soma_idade += idade

    if c == 1 and sexo in 'Mm':
        maior_idade = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome

    if sexo in 'Ff' and idade < 20:
        idade_mulher += 1
media_idade = soma_idade / 4
print(f'A média da idade do grupo é de {media_idade :.2f} anos.')
print(f'O Homem mais velho tem {maior_idade} anos e se chama {nome_velho}.')
print(
    f'O total de mulheres com menos de 20 anos é de {idade_mulher} mulheres.')
'''
