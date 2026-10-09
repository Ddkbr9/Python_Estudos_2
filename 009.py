#Leia três medidas e informe se elas podem formar um triângulo. Cada lado deve ser menor que
#a soma dos outros dois.
#DICA teste as três condições ao mesmo tempo com o operador and .

a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))

if a < b + c and b < a + c and c < a + b:
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')