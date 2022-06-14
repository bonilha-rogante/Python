from random import randrange
from time import sleep
# Pc pensa 1 número de 0 a 5 e usuário tenta descobrir

print('=====Desafio 028=====')

numero = randrange(0, 6)

tentativa = int(input('Digite o número: '))
print('PROCESSANDO...')
sleep(2)
if tentativa == numero:
    print(f'Parabéns! Você acertou. O número secreto era {numero}')
else:
    print(
        f'Você Errou! Você chutou {tentativa}.\nO número secreto era {numero}')
