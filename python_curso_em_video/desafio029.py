# leia a vel do carro. Se > 80 multado e valor é 7 reais a cada Km a mais


print('=====Desafio 029=====')

vel = float(input('O carro está andando a quantos Km\h:  '))

multa = (vel - 80) * 7

if vel > 80:
    print(
        f'Você está a {vel} Km\h e acima do limite de velocidade e foi multado.\nO valor da multa é de R${multa}. ')
else:
    print(f'Você está a {vel}Km\h e dentro do limite de velocidade.')
