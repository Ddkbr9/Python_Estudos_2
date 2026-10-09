#Leia o salário mensal e calcule o imposto por faixas progressivas: até 2.000 isento, até 3.000
#paga 7,5% sobre o excedente, até 4.500 paga 15% sobre o excedente, acima disso 22,5%.
#DICA o imposto incide apenas sobre a parte do salário dentro de cada faixa — não sobre o total.

salario = float(input('Digite o salário: '))

if salario <= 2000:
    imposto = 0
elif salario <= 3000:
    imposto = (salario - 2000) * 0.075
elif salario <= 4500:
    imposto = 1000 * 0.075 + (salario - 3000) * 0.15
else:
    imposto = 1000 * 0.075 + 1500 * 0.15 + (salario - 4500) * 0.225

print('Imposto: R$', round(imposto, 2))