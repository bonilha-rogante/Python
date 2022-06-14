# Leia nome e preço. A)Total gasto B)Custam + 1000 C)Nome do mais barato
total = tot_mil = menor = barato = cont = 0
while True:
    nome = input('Produto: ').strip()
    preco = float(input('Preço. R$ '))
    total += preco

    if preco > 1000:
        tot_mil += 1
    if cont == 1 and preco < menor:
        menor = preco
        barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = ('Você deseja continua [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break
print(
    f'O total gasto foi de R${total :.2f}\n{tot_mil} produtos custam mais de R$1000.00\nO produto mais barato é {barato}')
