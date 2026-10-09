#Leia um parágrafo e mostre qual palavra aparece mais vezes e quantas vezes ela aparece. Ignore pontuação. STRINGS 8
#DICA limpe a pontuação com .replace() , quebre com .split() e conte cada palavra
#com .count() — ou guarde as contagens em um dicionário.

texto = input('Digite um parágrafo: ').lower()

for sinal in '.,!?':
    texto = texto.replace(sinal, '')

palavras = texto.split()
maior = ''

for palavra in palavras:
    if palavras.count(palavra) > palavras.count(maior):
        maior = palavra

print(maior, palavras.count(maior))