# Leia idade e sexo, mostre quantos homens, quantas pessoas > 18 e quantas mulheres < 20

homem = maior = menor = 0
while True:
    print('=-' * 50)
    print('CADASTRO DE PESSOAS')
    print('=-' * 50)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        menor += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Você deseja continuar? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Maior de 18 {maior}\nHomens {homem}\nMulheres menores de 20{menor}')
