#Leia uma letra e informe se ela é vogal ou consoante.
#DICA converta para minúscula antes de testar, senão A escapa do teste.

letra = input('Digite uma letra: ').lower()

if letra in 'aeiou':
    print('Vogal')
else:
    print('Consoante')