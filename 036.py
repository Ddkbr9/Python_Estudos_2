#Leia dia, mês e ano e informe se a data existe, considerando meses de 30/31 dias e fevereiro em ano bissexto.
#DICA reaproveite a lógica do Exercício 31 e trate fevereiro como caso especial.

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if mes == 2:
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        limite = 29
    else:
        limite = 28
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    limite = 30
else:
    limite = 31

if mes >= 1 and mes <= 12 and dia >= 1 and dia <= limite:
    print('Data válida')
else:
    print('Data inválida')