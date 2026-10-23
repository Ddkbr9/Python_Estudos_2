# Pergunta: Crie converte(valor, moeda='R$'), que formata o valor com o símbolo da moeda e duas casas decimais.
# Dica: Use um parâmetro com valor padrão e :.2f na f-string.

def converte(valor, moeda='R$'):
    return f'{moeda} {valor:.2f}'


valor = float(input('Digite o valor: '))

print(converte(valor))