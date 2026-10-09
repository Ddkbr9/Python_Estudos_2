#Leia o salário de um funcionário e o percentual de aumento; mostre o valor do aumento
# e o novo salário formatado com duas casas decimais.
#DICA f'{valor:.2f}' controla as casas decimais na exibição.


salario = float(input('Digite o salário: '))
percentual = float(input('Digite o percentual de aumento: '))

aumento = salario * percentual / 100
novo_salario = salario + aumento

print(f'Aumento: R$ {round(aumento,2)}')
print(f'Novo salário: R$ {round(novo_salario,2)}')