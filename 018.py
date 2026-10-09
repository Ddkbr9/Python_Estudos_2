#Detector de palíndromo
#Leia uma palavra ou frase e informe se ela é um palíndromo (lê-se igual nos dois sentidos).
#Ignore espaços e diferença entre maiúsculas e minúsculas.
#DICA normalize primeiro (minúsculas, sem espaços), depois compare o texto com o seu reverso.


frase = input("Digite uma frase: ").strip().upper().replace(' ', '')

#2

if frase == frase[::-1]:
    print('É palindromo!')
else:
    print('Não é palindromo!')

#1

frase = frase.replace('', '').lower()

palindromo = True

for i in range(len(frase) // 2):
    if frase[i] != frase[len(frase) - 1 - i]:
        palindromo = False
        break

if palindromo:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")


