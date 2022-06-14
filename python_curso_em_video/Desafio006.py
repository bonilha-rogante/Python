# Leia um número  e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print(
    f'Você digitou {n}.\nO seu dobro é {dobro}\nO Seu triplo é {triplo}\nE sua raiz quadrada é {raiz :.2f}')


'''n1 = int(input('Digite um número: '))

d = n1 * 2
t = n1 * 3
# pode calcular a raiza quadrada com a função pow - rq = pow(n, (1/2))
rq = n1**(1/2)  # ou usar a função sqrt

print(
    f'Você digitou {n1}, \nseu dobro é {d}, \nseu triplo é {t} \ne sua raiz quadrada é {rq :.2f}.')'''
