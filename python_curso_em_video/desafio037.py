# Leia um número inteiro e escolha a base de conversão: 1-Binário 2-Octa 3-Hex
print('=====Desafio 037=====')

n = int(input('Digite o número que deseja converter: '))
print('Escolha para qual base deseja converter: ')
base = int(input('[1]-Binário\n[2]-Octal\n[3]-Hexadecimal\nSua opção é: '))

bin = bin(n)[2:]
oct = oct(n)[2:]
hex = hex(n)[2:]

if base == 1:
    print(
        f'Você escolheu converter o número {n} para a base BINÁRIA e o resultado é de {bin}.')
elif base == 2:
    print(
        f'Você escolheu converter o número {n} para a base OCTAL e o resultado é de {oct}.')
elif base == 3:
    print(
        f'Você escolheu converter o número {n} para a base HEXADECIMAL e o resultado é de {hex}.')
else:
    print('Comando inválido! Escolha novamente.')
