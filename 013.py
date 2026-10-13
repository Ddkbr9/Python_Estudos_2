#Leia o nome completo de uma pessoa e mostre: (1) tudo em maiúsculas, (2) tudo em minúsculas,
#(3) quantas letras ao todo sem contar os espaços, (4) quantas letras tem o primeiro nome.
#DICA .replace(' ', '') some com os espaços antes do len() ; .split() isola o primeiro nome.

nome = input('Digite seu nome completo: ')

print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
print(len(nome.split()[0]))