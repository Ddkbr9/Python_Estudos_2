#Leia duas notas, calcule a média e informe: aprovado (≥ 7), recuperação (≥ 5) ou reprovado.
#DICA teste do maior para o menor com elif ; assim você não precisa repetir os limites inferiores.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')