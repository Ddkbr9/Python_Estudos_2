#Leia três lados; se formarem um triângulo, informe se é equilátero, isósceles ou escaleno.
#DICA o if da validade envolve o bloco da classificação — use aninhamento.

a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print('Equilátero')
    elif a == b or a == c or b == c:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não forma um triângulo')