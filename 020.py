#Leia uma frase e mostre quantas vogais, quantas consoantes e quantos espaços ela tem.
#DICA um teste de pertencimento como letra in 'aeiou' resolve o primeiro grupo: verifique .isalpha() antes de contar consoante

frase = input('Digite uma frase: ')

vogais = 0
consoantes = 0
espacos = 0

for letra in frase:
    if letra in 'aeiou':
        vogais += 1
    elif letra.isalpha():
        consoantes += 1
    elif letra == ' ':
        espacos += 1

print('Vogais:', vogais)
print('Consoantes:', consoantes)
print('Espaços:', espacos)





