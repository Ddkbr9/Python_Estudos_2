#Leia um ano e informe se ele é bissexto: divisível por 4, exceto se for divisível por 100 e não por 400.
#DICA a regra inteira cabe em uma expressão só com and , or e parênteses.

ano = int(input('Digite um ano: '))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('Ano bissexto')
else:
    print('Não é bissexto')