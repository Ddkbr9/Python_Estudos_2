#Leia capital inicial, taxa mensal e número de meses; mostre o montante final e quanto foi ganho de juros. M = C·(1 + i)n

#ENTRADA, SAÍDA E OPERADORES


capital = float(input('Digite o capital inicial:  '))
taxa = float(input('Digite a taxa mensal:  '))
meses = int(input('Digite o número de meses:  '))

i = taxa / 100

montante = capital * (1 + i) ** meses
juros = montante - capital

print(f'Montante final:{round(capital,2)}')
print(f'Juros ganhos:{round(juros,2)}')