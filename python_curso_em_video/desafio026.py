# leia uma frase - Qts vezes aparece a, emque posiçaõ aparece a primeira vez, em que posição elva aparece a última

print('=====Desafio 026=====')

frase = input('Digite uma frase: ').lower().strip()

print(f"A Letra A aparece {frase.count('a')} vezes.")
print(f"A primeira vez que letra A aparece é na posição {frase.find('a')+1}")
print(f"A últimas vez que a letra A aparece é na posição {frase.rfind('a')+1}")
