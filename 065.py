# Crie uma tupla com os 10 filmes mais assistidos de todos os tempos e mostre:
# os 3 primeiros, os 2 últimos, a lista em ordem alfabética e a posição
# de 'O Rei Leão'.
#
# DICA: sorted() devolve uma nova lista ordenada sem alterar a tupla;
# .index() acha a posição.

def quebra_linha():
    print()

filmes = ('Avatar'
              ,'Vingadores: ultimato'
              ,'Homem-Aranha: Um Novo Dia '
              ,'Avatar: O Caminho da Água'
              ,'Ne zha 2'
              ,'Titanic'
              ,'Star Wars: Episódio VII - O Despertar da Força'
              ,'Vingadores: Guerra Infinita'
              ,'Homem Aranha: Sem Volta Pra Casa'
              ,'O Rei Leão')

#Os Três Primeiros:
quebra_linha()
print(f'Os 3 Primeiros Filmes São:')
for i in range(3):
    print(filmes[i])

#Os Dois Ultimos Mais Assistidos:
quebra_linha()
print(f'Os Dois Últimos Filmes mais Assistidos São:')
for i in range(8, 10):
    print(filmes[i])

#A Lista em Ordem Alfabética:
quebra_linha()
print(f'A Lista Dos Filmes em Ordem Alfabética:')
for i in sorted(filmes):
    print(i)

#Posição do Filme Rei Leão:
quebra_linha()
print(f'Posição do Filme Rei Leão:')
for i in range(len(filmes)):
    if filmes[i] == 'O Rei Leão':
        print('O Rei Leão está na posição', i + 1)