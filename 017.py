#Leia o nome completo e mostre apenas as iniciais em maiúsculo. Ex.: Luis Eulalio Tatin → L.E.T.
#DICA percorra a lista devolvida por .split() e pegue o caractere na posição 0 de cada parte.

nome = input('Digite seu nome completo: ')

partes = nome.split()
iniciais = ''

for parte in partes:
    iniciais = iniciais + parte[0].upper() + '.'

print(iniciais)