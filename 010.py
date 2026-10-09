#Leia peso e altura, calcule o IMC ( peso / altura2 ) e mostre a classificação: abaixo do peso,
#normal, sobrepeso ou obesidade.
#DICA encadeie as comparações em ordem crescente para não repetir testes.



peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)
imc = round(imc, 2)

print('Seu IMC é:', imc)

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Normal')
elif imc < 30:
    print('Sobrepeso')
else:
    print('Obesidade')