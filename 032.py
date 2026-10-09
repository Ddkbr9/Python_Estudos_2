#Leia o peso de uma encomenda e o estado de destino; calcule o frete conforme a faixa de peso, com 20% de acréscimo se o destino não for do Sudeste.
#DICA defina o valor base no if das faixas e aplique o acréscimo depois, em um teste separado.

peso = float(input('Digite o peso em kg: '))
estado = input('Digite o estado de destino: ').upper()

if peso <= 1:
    frete = 10
elif peso <= 5:
    frete = 20
else:
    frete = 30

if estado not in ['SP', 'RJ', 'MG', 'ES']:
    frete = frete * 1.2

print('Frete: R$', round(frete, 2))