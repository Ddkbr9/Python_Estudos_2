
import pandas as pd

#Série
#1
etiqueta = ['a','b','c']
dados = [1,2,3]

serie_1 = pd.Series(data=dados, index=etiqueta)
print(serie_1)

#2
d = {'a': 1, 'b': 2, 'c': 3}
serie_2 = pd.Series(data=d)
print(serie_2)



#Medalhas em Série
ser_1 = pd.Series(data=[1,2,3,4], index=['EUA','Alemanha','Brasil','Japão'])
ser_2 = pd.Series(data=[4,3,2,1], index=['EUA','Alemanha','Brasil','Japão'])

#Operações Matemáticas
ser3 = ser_1 + ser_2 * 2

#Acesso ao Conteúdo
print(ser3)
print(ser3['EUA'])

#Série Defeituosas
ser_4 = pd.Series(data=[4,3,2,], index=['EUA','Alemanha','Brasil'])
print(ser_1 + ser_4)

#1 linhas - Listas com Lista por frequência
base = [['João',54,'M'],
        ['Daniel',20,'M'],
        ['Cordélia',35,'F'],
        ['Thiago',69,'M']]

df_pessoas = pd.DataFrame(data=base, columns=['Nome','Idade','Sexo'])
print(df_pessoas)

#Dicionários - Cada valor será uma lista com todos os registros
base_dic = {'Nome':['João','Daniel','Cordélia','Thiago'],
            'Idade':[54,20,35,69],
            'Sexo':['M','M','F','M']}

df_pessoas = pd.DataFrame(data=base_dic)
print(df_pessoas)
