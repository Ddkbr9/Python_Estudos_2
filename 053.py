# Pergunta: Crie a função area(), que recebe a largura e a altura de um muro e mostra a área.
# Dica: Multiplique largura pela altura e use return ou print para apresentar o resultado.

def area(largura, altura):
    resultado = largura * altura
    print(f'A área é {resultado} m²')


largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

area(largura, altura)