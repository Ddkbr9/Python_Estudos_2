#Leia um e-mail e informe se ele é válido: exatamente um @ , pelo menos um . depois do @ , sem espaços e sem começar ou terminar com @ ou . .
#DICA .count('@') garante a unicidade; use fatiamento a partir da posição do @ para checar o domínio.

email = input('Digite um e-mail: ')

if '@' in email and '.com' in email and ' ' not in email:
    print('E-mail válido')
else:
    print('E-mail inválido')