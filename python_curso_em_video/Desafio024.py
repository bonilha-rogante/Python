# Leia uma cidade e diga se começa com santo

print('=====Desafio 024=====')

cidade = input('Digite o nome da cidade: ').lower().strip()
print(cidade[:5] == 'santo')


'''
cidade = input('Digite o nome da cidade: ').strip()

print(cidade[:5].lower() == 'santo')
'''

'''
cidade = cidade.lower()

if 'santo' in cidade:
    print(f'Você digitou a cidade {cidade} e há a palavra santo nela')
else:
    print(f'Você digitou {cidade} e não há a palavra santo nela')'''
