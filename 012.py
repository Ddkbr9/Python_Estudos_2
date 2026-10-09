#Leia as coordenadas (x, y) de dois pontos e calcule a distância entre eles. d = √((x2-x1)2 + (y2-y1)2)
#DICA math.hypot(dx, dy) faz a raiz da soma dos quadrados de uma vez — mas tente antes com math.sqrt .


import math

x1 = float(input('X1: '))
y1 = float(input('Y1: '))
x2 = float(input('X2: '))
y2 = float(input('Y2: '))

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f'A distância é: {d:.2f}')