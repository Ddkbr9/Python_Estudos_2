#Leia a idade de um atleta e classifique-o: até 9 mirim, até 14 infantil, até 19 júnior, até 25 sênior,acima disso master.
#DICA ordem crescente com elif evita que uma faixa "engula" a outra.

idade = int(input('Digite a idade: '))

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Júnior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')