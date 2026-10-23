# Pergunta: Leia um número e calcule seu fatorial.
# Dica: Comece com fatorial = 1 e multiplique pelos números de n até 1.

numero = int(input('Digite um número: '))

fatorial = 1

for i in range(numero, 0, -1):
    fatorial *= i

print(f'O fatorial de {numero} é {fatorial}')