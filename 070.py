# Leia 10 números e mostre a lista original, a lista ordenada, o maior,
# o menor e a soma.
#
# DICA: .sort() altera a lista original; sorted() cria uma cópia ordenada.

numeros = []

for i in range(10):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

lista_ordenada = sorted(numeros)

print('Lista original:', numeros)
print('Lista ordenada:', lista_ordenada)
print('Maior número:', max(numeros))
print('Menor número:', min(numeros))
print('Soma:', sum(numeros))