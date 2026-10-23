# Crie contador(inicio, fim, passo) que imprime a contagem no intervalo.
# Se o passo for 0, assuma 1; se o fim for menor que o início, conte para trás.
#
# DICA: ajuste o sinal do passo antes de montar o range.

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    if fim < inicio and passo > 0:
        passo = -passo
    elif fim > inicio and passo < 0:
        passo = -passo

    if passo > 0:
        fim = fim + 1
    else:
        fim = fim - 1

    for numero in range(inicio, fim, passo):
        print(numero, end=' ')

    print()


contador(1, 10, 2)
contador(10, 1, 2)