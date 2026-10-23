# Usando tuplas, leia um número de 0 a 15 e mostre-o escrito por extenso.
#
# DICA: a posição do número na tupla é o próprio número — nenhum if é necessário.

numeros = (
    'zero',
    'um',
    'dois',
    'três',
    'quatro',
    'cinco',
    'seis',
    'sete',
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze',
    'quatorze',
    'quinze'
)

numero = int(input('Digite um número de 0 a 15: '))
print(numeros[numero])