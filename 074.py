# Leia nome e duas notas de vários alunos, guarde em uma lista composta
# e exiba um boletim com nome, notas e média de cada um.
#
# DICA: cada item da lista principal é uma lista [nome, [n1, n2]];
# use índices para navegar.

alunos = []
quantidade = int(input('Quantos alunos? '))

for i in range(quantidade):
    nome = input('Nome: ')
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    alunos.append([nome, [n1, n2]])

for aluno in alunos:
    media = sum(aluno[1]) / 2
    print(aluno[0], aluno[1], 'Média:', media)