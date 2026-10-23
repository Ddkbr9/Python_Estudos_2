# Pergunta: Crie ficha(nome='<desconhecido>', gols=0) que imprime
# "O jogador X fez Y gol(s) no campeonato", funcionando mesmo se
# nada for informado.
# Dica: Teste com ficha(), ficha('Pelé') e ficha(gols=3)
# para validar os padrões.

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


ficha()
ficha('Pelé')
ficha(gols=3)