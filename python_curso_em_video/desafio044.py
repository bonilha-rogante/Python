# leia o preco, condição de pagamento - a vista dinehrio/cheque 10% desc, a vista cartão 5% desc, 2x cartão normal, 3x ou mais 20% juros.

print('=====Desafio 044=====')

valor = float(input('Qual o valor do produto R$: '))
print('Escolha sua forma de pagamento')
forma = int(input(
    '[1]Dinheiro/Cheque\n[2]Cartão\n[3]2x No Cartão\n[4]3x No Cartão\nOpção: '))

dinheiro = valor - (valor * 10 / 100)
cartao = valor - (valor * 5 / 100)
parcelado = (valor * 20 / 100) + valor

if forma == 1:
    print(
        f'Você escolheu a primeira forma de pagamento e terá 10% de desconto. O valor da compra será de R$ {dinheiro:.2f}.')
elif forma == 2:
    print(
        f'Você escolheu a segunda forma de pagamento e terá 5% de desconto. O valor da compra será de R$ {cartao :.2f}.')
elif forma == 3:
    print(
        f'Você escolheu a terceira forma de pagamento e o valor pago será o integral. R${valor :.2f}')
elif forma == 4:
    print(
        f'Você escolheu a quarta forma de pagamento e terá um acréscimo de 20% no valor. O total será de  R${parcelado :.2f}.')
else:
    print('Opção inválida!')
