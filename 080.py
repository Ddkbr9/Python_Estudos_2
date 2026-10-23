# Monte um sistema com menu para cadastrar produto (nome, quantidade, preço),
# listar o estoque, remover um produto e mostrar o valor total investido.
#
# DICA: uma lista composta guarda o estoque; encapsule cada opção do menu
# em uma função.

estoque = []

while True:
    opcao = input('1 Cadastrar, 2 Listar, 3 Remover, 4 Total, 0 Sair: ')

    if opcao == '1':
        nome = input('Produto: ')
        quantidade = int(input('Quantidade: '))
        preco = float(input('Preço: '))
        estoque.append([nome, quantidade, preco])

    elif opcao == '2':
        print(estoque)

    elif opcao == '3':
        nome = input('Produto para remover: ')
        for produto in estoque:
            if produto[0] == nome:
                estoque.remove(produto)
                break

    elif opcao == '4':
        total = 0
        for produto in estoque:
            total = total + produto[1] * produto[2]
        print(total)

    elif opcao == '0':
        break
