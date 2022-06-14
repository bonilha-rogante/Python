# Leia o preco e mostre 5% de desconto

print('=====Desafio 012=====')
valor = float(input('Digite o valor do produto. R$ '))
desconto = (valor / 100) * 5
total = valor - desconto
print(
    f'O valor do produto é de R${valor}.\nOs 5% de desconto é de R${desconto :.2f} e o valor total agora é de R${total :.2f}')


'''
preco = float(input('Digite o valor do produto, R$: '))

# Outra forma de calcular porcentagem = valor*porcentagem/100
desconto = (preco/100)*5
novo_preco = (preco - desconto)

print(
    f'O valor digitado foi R${preco :.2f}, o valor do desconto foi {desconto} e o novo valor é de R${novo_preco :.2f}')'''
