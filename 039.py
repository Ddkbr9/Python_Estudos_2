#Leia um número e conte de forma decrescente até 0, imprimindo Fogo! ao final.
#DICA range(n, -1, -1) percorre de trás para frente.

n = int(input('Digite um número: '))

for i in range(n, -1, -1):
    print(i)

print('Fogo!')