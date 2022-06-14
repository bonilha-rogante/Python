# calcule o IMC. abaixo 18.5 abaixo do peso, entre 18.5 e 25 peso ideal, 25 até 30 sobrepeso, 30 ate 40 obeso e acima de 40 mórbido

print('=====Desafio 043=====')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)
abaixo = imc < 18.5
ideal = imc < 25
sobrepeso = imc < 30
obeso = imc < 40

if abaixo:
    print(f'Seu IMC é de {imc :.1f} e você está abaixo do peso.')
elif ideal:
    print(f'Seu IMC é de {imc :.1f} e você está com o peso ideal')
elif sobrepeso:
    print(f'Seu IMC é de {imc :.1f} e você está com sobrepeso.')
elif obeso:
    print(f'Seu IMC é de {imc :.1f} e você está obeso')
else:
    print(f'Seu IMC é de {imc :.1f} e está com obesidade mórbida.')
