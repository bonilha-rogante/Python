# Veja a distância da viagem em Km. se Km <= 200 0.50 por km. Se Km > 200 0.45

print('=====Desafio 031=====')

km = float(input('Qual é a distância da sua viagem: '))

menor = km * 0.5
maior = km * 0.45

if(km <= 200):
    print(
        f'Sua viagem terá {km}Km e o valor da passagem será de R$ {menor :.2f}')
else:
    print(
        f'Sua viagem terá {km}Km e o valor da passagem será de R$ {maior :.2f}')
