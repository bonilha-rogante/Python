# crie jokenpo

print('=====Desafio 045=====')


from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)
print('Suas opções:\n[0]PEDRA\n[1]PAPEL\n[2]TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('-=' * 11)
print(f'O Computador escolheu {itens[maquina]}')
print(f'Você Jogou {itens[jogador]}')
print('-=' * 11)

if maquina == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('VOCÊ PERDEU!')
    else:
        print('Jogada Inválida!')

elif maquina == 1:
    if jogador == 0:
        print('VOCÊ PERDEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('Jogada Inválida!')

elif maquina == 2:
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('VOCÊ PERDEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada Inválida!')


'''
from random import randrange

print('Escolhar qual opção você jogar: ')

jogo = int(input('[1]Papel\n[2]Tesoura\n[3]Pedra\nOpção: '))
maquina = randrange(1, 4)
print(maquina)
papel = jogo == 1
tesoura = jogo == 2
pedra = jogo == 3

if maquina == jogo:
    print('Ops! Você jogaram o mesmo elemento. Tente Outra vez.')
elif jogo == 1 and maquina == 2:
    print(f'Você escolheu Papel e a Máquina Tesoura. Você perdeu')
elif jogo == 1 and maquina == 3:
    print('Você Escolheu Papel a Máquina Pedra. Você ganhou')
elif jogo == 2 and maquina == 1:
    print('Você escolheu Tesoura e a Máquina Papel. Você ganhou.')
elif jogo == 2 and maquina == 3:
    print('Você escolheu Tesoura e a Máquina Pedra. Você perdeu.')
elif jogo == 3 and maquina == 1:
    print('Você escolheu Pedra e Máquina Papel. Você perdeu')
elif jogo == 3 and maquina == 2:
    print('Você escolheu Pedra e a Máquina Tesoura. Você ganhou.')
'''
