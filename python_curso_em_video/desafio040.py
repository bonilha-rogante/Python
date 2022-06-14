# leia 2 notas e calcule a média - <5 reprovado,  5 até 6.9 recuperação e >7 aprovado
print('=====Desafio 040=====')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

reprovado = media < 5
recuperacao = media < 7

if reprovado:
    print(
        f'Suas notas foram {n1} e {n2}, sua média foi {media :.2f} e você está REPROVADO.')
elif recuperacao:
    print(
        f'Suas notas foram {n1} e {n2}, sua média foi {media :.2f} e você está de RECUPERAÇÃO.')
else:
    print(
        f'PARABÉNS! Suas notas foram {n1} e {n2}, sua média foi {media :.2f} e você foi APROVADO!')
