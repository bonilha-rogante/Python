# Perguntar o valor da casa, salário, qtos anos pagar, não pode excerder 30% do salário.

print('=====Desafio 036=====')

casa = float(input('Digite o valor da casa que deseja comprar R$ '))
sal = float(input('Digite o valor do salário R$ '))
ano = int(input('Em quantos anos pretende pagar a casa: '))

mes = ano * 12
prestacao = casa / mes
parcela = sal * 30 / 100
aceito = parcela >= prestacao

if aceito:
    print(
        f'Parabéns! Você foi aprovado. O valor da casa é de R${casa :.2f}, as parcelas serão de R${prestacao:.2f} o que é menos que 30% do seu salário que é R${parcela}')
else:
    print(
        f'Infelizmente você não foi aprovado. O valor da casa é de R${casa :.2f}, as mensalidades serão de R${prestacao:.2f} o que é mais do que 30% do seu salário que é de R${parcela:.2f}')
