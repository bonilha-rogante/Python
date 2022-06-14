
dado = input("Digite algo: ")

print(f"O tipo primitivo desse valor é{type(dado)}")
print(f"É Alfanumérico? {dado.isalnum()}")
print(f"É alfabético? {dado.isalpha()}")
print(f"É decimal? {dado.isdecimal()}")
print(f"É um digito? {dado.isdigit()}")
print(f"Está tudo em minúscula? {dado.islower()}")
print(f"É numérico? {dado.isnumeric()}")
print(f"Só tem espaços? {dado.isspace()}")
print(f"Está capitalizada? {dado.istitle()}")
print(f"Está em maiúscula? {dado.isupper()}")
