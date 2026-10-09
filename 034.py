#Leia um valor de saque entre 10 e 600 e informe quantas notas de 100, 50, 20 e 10 serão
#entregues, usando o menor número de cédulas. Recuse valores impossíveis.
#DICA valide primeiro (múltiplo de 10 e dentro da faixa) e só então faça as divisões sucessivas.

valor = int(input('Digite o valor do saque: '))

if valor < 10 or valor > 600 or valor % 10 != 0:
    print('Valor inválido')
else:
    for nota in [100, 50, 20, 10]:
        quantidade = valor // nota
        valor = valor % nota

        if quantidade > 0:
            print(quantidade, 'nota(s) de R$', nota)