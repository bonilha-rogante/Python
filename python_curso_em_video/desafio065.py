# leia vários número. mostre a média entr todos, maior, menor . Deve perguntar se quer continuar ou não

print('=====Desafio 065=====')

res = 'S'

soma = quant = media = maior = menor = 0

while res in 'S':
    n = float(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    res = input('Quer continuar? [S/N] ').upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant :.2} números e a média foi {media :.2}.')
