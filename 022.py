#Leia uma palavra e um número de deslocamento; devolva a palavra cifrada, deslocando cada
#letra no alfabeto. abc com deslocamento 2 → cde .
#DICA ord() transforma letra em número e chr() faz o caminho de volta; use % 26 para dar a volta no alfabeto.

palavra = input('Digite uma palavra: ')
n = int(input('Digite o deslocamento: '))
cifra = ''

for letra in palavra:
    nova = (ord(letra) - 97 + n) % 26 + 97
    cifra += chr(nova)

print(cifra)