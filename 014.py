#Caçando a letra "a"
#Leia uma frase e mostre quantas vezes a letra "a" aparece, em que posição aparece pela
#primeira vez e em que posição aparece pela última.
#DICA .count() , .find() e .rfind() resolvem os três itens.


frase = input('Digite uma frase: ')

print('Quantidade de letras a:', frase.lower().count('a'))
print('Primeira posição:', frase.lower().find('a'))
print('Última posição:', frase.lower().rfind('a'))