# Leia o nome e o QI de várias pessoas, guardando tudo em uma lista.
# Ao final, mostre quantas foram cadastradas, quem tem o maior QI
# e quem tem o menor.
#
# DICA: guarde uma cópia (dados[:]) na lista principal; sem a cópia,
# todos os registros ficam iguais.

pessoas = []

quantidade = int(input('Quantas pessoas deseja cadastrar? '))

for i in range(quantidade):
    nome = input('Nome: ')
    qi = int(input('QI: '))
    pessoas.append([nome, qi])

maior = pessoas[0]
menor = pessoas[0]

for pessoa in pessoas:
    if pessoa[1] > maior[1]:
        maior = pessoa
    if pessoa[1] < menor[1]:
        menor = pessoa

print('Pessoas cadastradas:', len(pessoas))
print('Maior QI:', maior[0], '-', maior[1])
print('Menor QI:', menor[0], '-', menor[1])