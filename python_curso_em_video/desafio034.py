# Leia Sal e se > 1250 + 10%. se < + 15%

print('=====Desafio 034=====')

sal = float(input('Digite o salário: '))

dez = (sal * 10 / 100) + sal
quinze = (sal * 15 / 100) + sal

if(sal > 1250):
    print(
        f'Seu salário é de R${sal :.2f} e teve um aumento de 10%.\nSeu novo salário é de R${dez :.2f}.')
else:
    print(
        f'Seu salário é de R${sal :.2f} e teve um aumento de 15%.\nSeu novo salário é de R${quinze :.2f}')
