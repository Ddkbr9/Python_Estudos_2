# Pergunta: Monte um menu com as opções Somar, Multiplicar, Maior e Sair.
# Dica: Use while True, if, elif e break para controlar o menu.

while True:
    print('\n1 - Somar')
    print('2 - Multiplicar')
    print('3 - Maior')
    print('4 - Sair')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 4:
        break

    if opcao < 1 or opcao > 4:
        print('Opção inválida!')
        continue

    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    if opcao == 1:
        print(f'Soma: {n1 + n2}')
    elif opcao == 2:
        print(f'Multiplicação: {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'Maior: {n1}')
        elif n2 > n1:
            print(f'Maior: {n2}')
        else:
            print('Os números são iguais!')

print('Programa encerrado!')