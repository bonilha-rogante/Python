# Leia o salario e mostra o salario com 15% de aumento

print('=====Desafio 013=====')

salario = float(input('Digite seu salário R$ '))

porcentagem = salario / 100 * 15
total = salario + porcentagem

print(
    f'Seu salário é de R${salario}.\nO aumento de 15% é de R${porcentagem:.2f}\nSeu novo salário será de R${total:.2f}')


'''
sal = float(input('Digite o seu salário: R$ '))

porcentagem = (sal/100)*15  # alterar a ordem também funciona = sal * 15 / 100
novo_salario = sal + porcentagem


print(
    f'O salário digitado foi R${sal :.2f}, o aumento foi de 15%, totalizando R${porcentagem :.2f} e seu novo salário é de R${novo_salario :.2f}')'''
