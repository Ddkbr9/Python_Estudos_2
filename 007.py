#Troco da máquina Leia um valor inteiro em centavos e mostre quantas moedas
#de 50, 25, 10, 5 e 1 centavo são necessárias usando o menor número de moedas.
#DICA vá da maior moeda para a menor, sempre com // para a quantidade e % para o resto.

centavos = int(input('Digite seus Centavos: '))

moedas50 = centavos // 50
resto = centavos % 50

moedas25 = centavos // 25
resto = centavos % 25

moedas10 = centavos // 10
resto = centavos % 10

moedas5 = centavos // 5
resto = centavos % 5

moedas1 = centavos // 1
resto = centavos % 1

print(f'quantidade de moedas de 50 centavos é {moedas50},De 25 é {moedas25},De 10 é  {moedas10},De 5 é  {moedas5} e de 1 é {moedas1}')




