#Leia um CPF no formato 12345678900 e exiba-o como 123.456.789-00 .
#DICA o fatiamento cpf[0:3] , cpf[3:6] ... recorta cada bloco.

cpf = input("Digite seu CPF: ")

cpf_formatado = cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:11]

print(cpf_formatado)