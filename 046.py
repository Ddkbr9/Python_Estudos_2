# Pergunta: Leia 3 números e ofereça opções para somar, multiplicar, mostrar o maior, ler novos números ou sair.
# Dica: Use dois while para controlar a leitura dos números e o menu.

sair = False

while not sair:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))

    while True:
        print('\n1 - Somar')
        print('2 - Multiplicar')
        print('3 - Mostrar o maior')
        print('4 - Ler novos números')
        print('5 - Sair')

        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            print(f'Soma: {n1 + n2 + n3}')
        elif opcao == 2:
            print(f'Multiplicação: {n1 * n2 * n3}')
        elif opcao == 3:
            print(f'Maior número: {max(n1, n2, n3)}')
        elif opcao == 4:
            break
        elif opcao == 5:
            sair = True
            break
        else:
            print('Opção inválida!')

print('Programa encerrado!')