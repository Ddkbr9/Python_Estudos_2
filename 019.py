#Leia uma senha e informe se ela é forte: mínimo 8 caracteres, ao menos uma letra maiúscula, uma minúscula e um dígito.
#DICA percorra a senha marcando flags booleanas e use .isupper() , .islower() e .isdigit() em cada caractere.

senha = input('Digite uma senha: ')

maiuscula = False
minuscula = False
numero = False

for letra in senha:
    if letra.isupper():
        maiuscula = True
    elif letra.islower():
        minuscula = True
    elif letra.isdigit():
        numero = True

if len(senha) >= 8 and maiuscula and minuscula and numero:
    print('Senha forte!')
else:
    print('Senha fraca!')







