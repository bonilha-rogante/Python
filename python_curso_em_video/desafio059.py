# leia 2 valores e mostre um menu na tela = [1]Soma [2]multiplicar [3]maior [4] novos número [5] sair do programa
print('=====Desafio 059=====')


n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

soma = n1 + n2
mult = n1 * n2
opcao = 0
print('Menu de Opções: ')

while opcao != 5:
    opcao = int(input(
        '[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Números\n[5]Sair do programa\nEscolha: '))
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é de {soma}.')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} é de {mult}.')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'Entre {n1} e {n2} o maior número é {n1}')
        else:
            maior = n2
            print(f'Entre {n1} e {n2} o maior número é {n2}')
    if opcao == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
print('Fim')
