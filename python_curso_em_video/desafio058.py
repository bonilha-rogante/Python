# melhore o desafio 28. pensar um número entre 1 e 10. \Tentar até acerta e mostrar quantos chutes foram necessários
from random import randint
computador = randint(1, 10)
tentativa = 0
acertou = False
while acertou == False:
    tentativa += 1
    print(f'Tentativa {tentativa}')
    numero = int(input('Digite seu chute: '))
    if numero == computador:
        acertou == True
        print(
            f'Parabéns! Você acertou. O número era {numero}. Você fez em {tentativa} tentativas')
    else:
        if numero < computador:
            print(f'O número é maior do que {numero}')
        if numero > computador:
            print(f'O número é menor do que {numero}')
print('Parabéns! ')

'''from random import randint
print('=====Desafio 058=====')

acertou = False
tentativas = 0

n = randint(1, 10)

while not acertou:
    print(f'Tentativa {tentativas}')
    chute = int(input('Digite seu chute: '))
    tentativas += 1
    if chute == n:
        acertou = True
        print(
            f'Você acertou o número secreto {n} e fez em {tentativas} tentativas')
    else:
        if chute < n:
            print(f'Ops! O número é maior do que {chute}')
        elif chute > n:
            print(f'Ops! O número é menor do que {chute} ')
print('Parabéns!')'''
