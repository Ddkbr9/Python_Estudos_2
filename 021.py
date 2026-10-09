#Leia uma frase bagunçada (com espaços sobrando nas pontas e capitalização aleatória) e
#devolva-a limpa, com cada palavra iniciando em maiúscula.
#DICA .strip() limpa as bordas e .title() ajusta as iniciais.

frase = input('Digite uma frase: ')

frase = frase.strip().title()

print(frase)
